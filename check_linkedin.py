import requests

api_key = 'bNzs-cEzZxT3WadkdArjHQ'
headers = {'Authorization': 'Bearer ' + api_key}
api_endpoint = 'https://nubela.co/proxycurl/api/linkedin/company'
params = {
    'url': 'https://www.linkedin.com/company/google/',
    
}
response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)
print(response.json())