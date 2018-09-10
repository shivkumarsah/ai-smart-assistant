import requests

print(requests.get('http://172.20.10.2:8080/query2engine', params=dict(query='testing shiv ABC')).content)