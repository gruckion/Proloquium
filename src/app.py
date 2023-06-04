

import chainlit as cl
from dotenv import load_dotenv
from langchain import LLMChain, LLMMathChain, OpenAI, PromptTemplate, SerpAPIWrapper
from langchain.agents import Tool, initialize_agent
from langchain.chat_models import ChatOpenAI

load_dotenv()

template = """Question: {question}

Answer: Let's think step by step."""

@cl.langchain_factory
def factory():
    llm = OpenAI(temperature=0, streaming=True)
    flag = True

    if flag:
        prompt = PromptTemplate(template=template, input_variables=["question"])
        return LLMChain(prompt=prompt, llm=llm, verbose=True)


    chat_llm = ChatOpenAI(temperature=0)
    search = SerpAPIWrapper()
    llm_math_chain = LLMMathChain.from_llm(llm=chat_llm, verbose=True)

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
        tools, llm, agent="chat-zero-shot-react-description", verbose=True
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
    pass
    # Sending an action button within a chatbot message
    # actions = [
    #     cl.Action(name="action_button", value="example_value", description="Click me!")
    # ]

    # cl.Message(content="Interact with this action button:", actions=actions).send()

    # res = cl.AskUserMessage(content="What is your name?", timeout=10).send()
    # if res:
    #     cl.Message(
    #         content=f"Your name is: {res['content']}",
    #     ).send()


    file = None

    # Wait for the user to upload a file
    while file is None:
        file = cl.AskFileMessage(
            content="Please upload a text file to begin!", accept=["text/plain"]
        ).send()
    # Decode the file
    text = file.content.decode("utf-8")

    # Let the user know that the system is ready
    cl.Message(
        content=f"`{file.name}` uploaded, it contains {len(text)} characters!"
    ).send()
