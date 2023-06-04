

import chainlit as cl
from dotenv import load_dotenv
from langchain import LLMMathChain, OpenAI, SerpAPIWrapper
from langchain.agents import Tool, initialize_agent
from langchain.chat_models import ChatOpenAI

load_dotenv()

template = """Question: {question}

Answer: Let's think step by step."""

@cl.langchain_factory
def factory():
    llm = ChatOpenAI(temperature=0)
    llm1 = OpenAI(temperature=0)
    search = SerpAPIWrapper()
    llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="useful for when you need to answer questions about current events. You should ask targeted questions",
        ),
        Tool(
            name="Calculator",
            func=llm_math_chain.run,
            description="useful for when you need to answer questions about math",
        ),
    ]
    return initialize_agent(
        tools, llm1, agent="chat-zero-shot-react-description", verbose=True
    )

@cl.action_callback("action_button")
def on_action(action):
    cl.Message(content=f"Executed {action.name}").send()

    # Sending an image with the local file path
    elements = [
    cl.LocalImage(name="image1", display="inline", path="./assets/cat.jpg")
    ]

    cl.Message(content="Look at this local image!", elements=elements).send()

    # Optionally remove the action button from the chatbot user interface
    action.remove()

@cl.on_chat_start
def start():
    # Sending an action button within a chatbot message
    actions = [
        cl.Action(name="action_button", value="example_value", description="Click me!")
    ]

    cl.Message(content="Interact with this action button:", actions=actions).send()
