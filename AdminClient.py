import requests
import json

data = {"3":"[[0,10],[2,9]]"}
data = json.dumps(data)
AddNodeUrl = "http://127.0.1.1:7021/"
response = requests.post(url=AddNodeUrl,data=bytes(str(data),'ascii'))
print(response.content.decode())


