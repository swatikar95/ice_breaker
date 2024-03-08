from langchain.utilities import SerpAPIWrapper
from dotenv import load_dotenv
import os

# Make sure the .env file is in the current directory or provide the correct path
load_dotenv()

# Custom wrapper class for SerpAPI that expects an API key upon initialization
class CustomSerpAPIWrapper(SerpAPIWrapper):
    def __init__(self, serpapi_api_key: str):
        # Pass the serpapi_api_key to the superclass constructor
        super(CustomSerpAPIWrapper, self).__init__(serpapi_api_key=serpapi_api_key)

    @staticmethod
    def _process_response(res: dict) -> str:
        """Process response from SerpAPI."""
        if "error" in res.keys():
            raise ValueError(f"Got error from SerpAPI: {res['error']}")

        toret = "No good search result found"  # Default response
        if "answer_box" in res.keys():
            answer_box = res["answer_box"]
            if "answer" in answer_box.keys():
                toret = answer_box["answer"]
            elif "snippet" in answer_box.keys():
                toret = answer_box["snippet"]
            elif "snippet_highlighted_words" in answer_box.keys():
                toret = answer_box["snippet_highlighted_words"][0]

        elif "sports_results" in res.keys() and "game_spotlight" in res["sports_results"].keys():
            toret = res["sports_results"]["game_spotlight"]
        elif "knowledge_graph" in res.keys() and "description" in res["knowledge_graph"].keys():
            toret = res["knowledge_graph"]["description"]
        elif "organic_results" in res and "snippet" in res["organic_results"][0].keys():
            toret = res["organic_results"][0]["link"]

        return toret

def get_profile_url(name: str):
    """Searches for Linkedin or Twitter Profile Page."""
    serpapi_api_key = os.getenv('SERP_API_KEY')
    if not serpapi_api_key:
        raise ValueError("SERP_API_KEY environment variable not set")
    
    search = CustomSerpAPIWrapper(serpapi_api_key=serpapi_api_key)
    res = search.run(name)
    return res

# Example usage
# profile_url = get_profile_url("John Doe LinkedIn")
# print(profile_url)
