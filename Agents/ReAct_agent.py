import hf_local as hf
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent,AgentExecutor
from langchain import hub
import requests

search_engine=DuckDuckGoSearchRun()

@tool
def get_weather(city:str) ->str:
    """this tool can get the latest weather condition for provided city"""

    url=f'https://api.weatherstack.com/current?access_key=4d1d8ae207a8c845a52df8a67bf3623e&query={city}'
    resp=requests.get(url)

    return resp.json()

prompt = hub.pull("hwchase17/react")

agents = create_react_agent(
    model=hf.get_hf_local_model(),
    tools=[search_engine,get_weather],
    prompt=prompt
)

executer= AgentExecutor(
    agent=agents,
    tools=[search_engine,get_weather],
    verbose=True
)

response = executer.invoke({"input":"hii, can you tell me the capital of madhya pradesh and also find the weather condition of the same capital ?"})

print(response)