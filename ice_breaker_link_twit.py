import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linked_profile
from third_parties.twitter import scrape_user_tweets

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent

name = "Harrison Chase"
if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
    print("hello")
    os.environ.get("OPENAI_API_KEY")
  

    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linked_data = scrape_linked_profile(linked_profile_url=linkedin_profile_url)

    twitter_user_name = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=twitter_user_name,num_tweets=2)

    summary_template = """
    given the linkedin information {linkedin_information} and twitter information {twitter_information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about the
    3. A topic that may interest them
    4. 2 creative Ice breakers to open a conversation with them
    """

    summary_prompt_template = PromptTemplate(input_variables=["linkedin_information","twitter_information"],template=summary_template)
    llm = ChatOpenAI(temperature=0,model_name="gpt-3.5-turbo") 

    chain = LLMChain(llm=llm,prompt=summary_prompt_template)
    
    
    print(chain.run(linked_information=linked_data,twitter_information=tweets))


