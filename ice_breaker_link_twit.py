import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from third_parties.linkedin import scrape_linked_profile
from third_parties.twitter import scrape_user_tweets
from chain.custom_chain import (
    get_summary_chain,
    get_interests_chain,
    get_ice_breaker_chain
)

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from output_parser import (
    summary_parser,
    topics_of_interest,
    ice_breaker_parser,
    Summary,
    IceBreaker,
    TopicOfInterest
)

def ice_breaker(name:str)->tuple[Summary,IceBreaker,TopicOfInterest,str]:
    load_dotenv()
    os.environ.get("OPENAI_API_KEY")
  

    linkedin_profile_url = linkedin_lookup_agent(name=name)
    linked_data = scrape_linked_profile(linked_profile_url=linkedin_profile_url)

    # twitter_user_name = twitter_lookup_agent(name=name)
    # tweets = scrape_user_tweets(username=twitter_user_name,num_tweets=2)

    summary_chain = get_summary_chain()
    summary_and_facts = summary_chain.run(
        information=linked_data
    )
    summary_and_facts = summary_parser.parse(summary_and_facts)

    interest_chain = get_interests_chain()
    interests = interest_chain.run(
        information = linked_data
    )
    interests = topics_of_interest.parse(interests)

    ice_breaker_chain = get_ice_breaker_chain()
    ice_breakers = ice_breaker_chain.run(
        information=linked_data
    )
    ice_breakers = ice_breaker_parser.parse(ice_breakers)

    return(
        summary_and_facts,
        interests,
        ice_breakers,
        linked_data.get("profile_pic_url")
    )

if __name__ == "__main__":
    pass
