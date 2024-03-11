import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linked_profile
from third_parties.twitter import scrape_user_tweets

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
    print("hello")
    os.environ.get("OPENAI_API_KEY")
  

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


