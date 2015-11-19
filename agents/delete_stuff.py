import requests
# base url
base_url = 'http://141.211.39.87:8089'
# username default
username = 'admin'
# password default
password = 'admin'

from tqdm import *


'''
set up session in archivesspace using requests'''

# get authorization and return as json
authorization = requests.post(base_url + '/users/' + username + '/login?password=' + password).json()
# get the session token
session_token = authorization["session"]
# create the headers we'll need for posting
headers = {'X-ArchivesSpace-Session': session_token}


people_ids = requests.get('http://141.211.39.87:8089/agents/people?all_ids=true', headers=headers).json()

for i in tqdm(people_ids[5:], desc="People"):
    delete_ = requests.delete('http://141.211.39.87:8089/agents/people/' + str(i), headers=headers)

corp_ids = requests.get('http://141.211.39.87:8089/agents/corporate_entities?all_ids=true', headers=headers).json()

for i in tqdm(corp_ids, desc="Corporate Entities"):
    delete_ = requests.delete('http://141.211.39.87:8089/agents/corporate_entities/' + str(i), headers=headers)

fam_ids = requests.get('http://141.211.39.87:8089/agents/families?all_ids=true', headers=headers).json()

for i in tqdm(fam_ids, desc="Families"):
    delete_ = requests.delete('http://141.211.39.87:8089/agents/families/' + str(i), headers=headers)
