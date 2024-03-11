from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent,Tool,AgentType
from langchain import hub
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)

from tools.tools import get_profile_url

def lookup(name:str)->str:
    llm = ChatOpenAI(temperature=0,model_name='gpt-3.5-turbo')
    template = """given the full name {name_of_person} I want you to get it me a link to their Twitter profile page.
    Final answer should contain only the person's usename"""

    prompt_template = PromptTemplate(template=template,input_variables=['name_of_person'])

    tools_for_agent = [
        Tool(
            name = "Crawl Google 4 Twitter profile page",
            func = get_profile_url,
            description="useful for when you need the Twitter page URL"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt) 
    agent_executor = AgentExecutor(agent=agent,tools=tools_for_agent,verbose=True)

    result = agent_executor.invoke(
        input={"input":prompt_template.format_prompt(name_of_person=name)}
    )

    twitter_user_name = result["output"]
    return twitter_user_name


    return "Twitter username: @elonmusk"