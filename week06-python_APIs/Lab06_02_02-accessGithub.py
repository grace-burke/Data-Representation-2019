import requests
import json


apiKey = 'd42864d9a3fe416cb346e5630781ceaf262e7bf5'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename ="repo.json"

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()

file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)