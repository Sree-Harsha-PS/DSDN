import requests
import json

data = {"3":"[[0,10],[2,9]]"}
data = json.dumps(data)
url = "http://127.0.1.1:3000/"
response = requests.get(url=url+"GetManagerLeaderIP",data=b'getLeaderManagerIP')
print(response.content.decode())


