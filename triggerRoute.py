import requests
import json
url = "http://127.0.1.1:10001/GetNextNode"
data = {
    "Source":"http://127.0.1.1:10001/",
    "Current":"",
    "Destination":"http://127.0.1.1:10002/"
}
data = json.dumps(data)
res = requests.post(url=url,data=data)