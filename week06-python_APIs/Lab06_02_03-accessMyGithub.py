import requests
import json

apiKey = ' 79ba98966d331141a6f654e169ea79865e562c23'
url = 'https://github.com/grace-burke/Data-Representation-2019'
filename ="myrepo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)