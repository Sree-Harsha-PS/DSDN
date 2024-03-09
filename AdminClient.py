import requests
import json

data = {"3":"[[0,10],[2,9]]"}
data = json.dumps(data)
url = "http://127.0.1.1:7011/"
# response = requests.get(url=url+"GetManagerLeaderIP",data=b'getLeaderManagerIP')
# response = requests.get(url=url+"GetManagerLeaderIP",data=b'getLeaderManagerIP')

response = requests.post(url=url+"AddNode",data=data)
response = requests.post(url=url+"GetOTPFromAdmin",data=data)
print(response.content.decode())


