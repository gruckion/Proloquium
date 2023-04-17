from langchain.agents import initialize_agent, load_tools
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)


tools = load_tools([
    "serpapi",
    "llm-math",
    "wikipedia",
    "terminal",
    "python_repl",
    # "wolfram-alpha", WOLFRAM_ALPHA_APPID
    "requests",
    "pal-math",
    "pal-colored-objects",
    "open-meteo-api",
    # "news-api", news_api_key
    # "tmdb-api", tmdb_bearer_token
    # "google-search", GOOGLE_API_KEY
    # "searx-search", SEARX_HOST
    # "google-serper", SERPER_API_KEY
    # "podcast-api", listen_api_key
    # "openweathermap-api", doesn't exist?
], llm=llm)


agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Wolfram Alpha: A wrapper around Wolfram Alpha. Useful for when you need to answer questions about math, science, and other subjects. Input should be a search query.
# News API: A wrapper around the News API. Useful for when you need to answer questions about news. Input should be a search query.
# TMDB API: A wrapper around the TMDB API. Useful for when you need to answer questions about movies. Input should be a search query.
# Google Search: A wrapper around the Google Search API. Useful for when you need to answer questions about current events. Input should be a search query.
# Searx Search: A wrapper around the Searx Search API. Useful for when you need to answer questions about current events. Input should be a search query.
# Google Serper: A wrapper around the Google Serper API. Useful for when you need to answer questions about current events. Input should be a search query.
# Podcast API: A wrapper around the Podcast API. Useful for when you need to answer questions about podcasts. Input should be a search query.
# OpenWeatherMap API: A wrapper around the OpenWeatherMap API. Useful for when you need to answer questions about weather. Input should be a search query.


agent.agent.llm_chain.prompt.template = """
Answer the following questions as best you can. You have access to the following tools:

Terminal: Executes commands in a terminal. Input should be valid commands, and the output will be any output from running that command. Might need to install the program using brew if it is not available.
Requests: A wrapper around the Requests library. Useful for when you need to answer questions about HTTP requests. Input should be valid Python code, and the output will be any output from running that code.
Python REPL: A Python REPL. Useful for when you need to answer questions about Python. Input should be valid Python code, and the output will be any output from running that code.
Calculator: Useful for when you need to answer questions about math.
Wikipedia: A wrapper around Wikipedia. Useful for when you need to answer general questions about people, places, companies, historical events, or other subjects. Input should be a search query.
Search: A search engine. Useful for when you need to answer questions about current events. Input should be a search query.
PAL Math: A wrapper around PAL Math. Useful for when you need to answer questions about math. Input should be a search query.
PAL Colored Objects: A wrapper around PAL Colored Objects. Useful for when you need to answer questions about colors. Input should be a search query.
Open Meteo API: A wrapper around the Open Meteo API. Useful for when you need to answer questions about weather. Input should be a search query.

Use the following format:

Question: the input question you must answer

Thought: you should always think about what to do
Action: the action to take, should be one of [Terminal, Requests, Python REPL, Calculator, Wikipedia, Search, PAL Math, PAL Colored Objects, Open Meteo API]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""

agent.run("What city am I in right now?")
