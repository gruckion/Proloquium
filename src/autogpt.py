
import chainlit as cl
from dotenv import load_dotenv
import faiss
from langchain.agents import Tool
from langchain.chat_models import ChatOpenAI
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings
from langchain.experimental import AutoGPT
from langchain.tools.file_management.read import ReadFileTool
from langchain.tools.file_management.write import WriteFileTool
from langchain.utilities import SerpAPIWrapper
from langchain.vectorstores import FAISS

load_dotenv()

# Tools the langchain agent will have access to
search = SerpAPIWrapper()
tools = [
    Tool(
        name="search",
        func=search.run,
        description="useful for when you need to answer questions about current events. You should ask targeted questions",
    ),
    WriteFileTool(),
    ReadFileTool(),
]


# Define your embedding model
embeddings_model = OpenAIEmbeddings()
# Initialize the vectorstore as empty

embedding_size = 1536
index = faiss.IndexFlatL2(embedding_size)


# Create the agent with the chainlit decorator
@cl.langchain_factory
def agent():
    vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})
    agent = AutoGPT.from_llm_and_tools(
        ai_name="Tom",
        ai_role="Assistant",
        tools=tools,
        llm=ChatOpenAI(temperature=0, streaming=True),
        memory=vectorstore.as_retriever(),
    )
    # Set verbose to be true
    agent.chain.verbose = True
    return agent


@cl.langchain_run
def run(agent, message):
    res = agent.run([message])
    cl.Message(content=res).send()
