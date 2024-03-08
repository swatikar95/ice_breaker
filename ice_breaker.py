import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linked_profile

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
    print("hello")
    os.environ.get("OPENAI_API_KEY")
    # print(os.environ["OPENAI_API_KEY"])
    # information = """
    # Elon Reeve Musk (/ˈiːlɒn/; EE-lon; born June 28, 1971) is a businessman and investor. 
    # He is the founder, chairman, CEO, and CTO of 
    # SpaceX; angel investor, CEO, product architect, and former chairman of Tesla, Inc.; 
    # owner, executive chairman, and CTO of X Corp.; founder of the Boring Company and xAI; 
    # co-founder of Neuralink and OpenAI; and president of the Musk Foundation. He is one of the 
    # wealthiest people in the world, with an estimated net worth of US$232 billion as of December 2023, according to the Bloomberg Billionaires Index, and $182.6 billion according to Forbes, primarily from his ownership stakes in Tesla and SpaceX.
    # """
    # res = chain.invoke(input={"information":information})
    # print(res)
    # print(linked_data.json())

    linkedin_profile_url = linkedin_lookup_agent(name="Swati Kar Clarkson University")

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about the
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"],template=summary_template)
    llm = ChatOpenAI(temperature=0,model_name="gpt-3.5-turbo") 

    chain = LLMChain(llm=llm,prompt=summary_prompt_template)
    
    
    linked_data = scrape_linked_profile(
        linked_profile_url = linkedin_profile_url 
    )
    print(chain.run(information=linked_data))


