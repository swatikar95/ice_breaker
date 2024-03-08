import os
import requests
from dotenv import load_dotenv

def scrape_linked_profile(linked_profile_url:str):
    """scrape information from Linked profiles.
    Manually scrope the information from the linkedIn profile"""

    api_key = 'bNzs-cEzZxT3WadkdArjHQ'

    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_doc = {'Authorization': 'Bearer ' + api_key}

    response = requests.get(
        api_endpoint,params = {"url":linked_profile_url},headers=header_doc
    )

    data = response.json()
    data = {
        k: v
        for k,v in data.items()
        if v not in ([],"",None)
        and k not in ["people_also_viewed","certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
