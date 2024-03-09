import requests
import json
url = "http://127.0.1.1:10007/GetNextNode"
data = {
    "Source":"http://127.0.1.1:10007/",
    "Current":"http://127.0.1.1:10007/",
    "Destination":"http://127.0.1.1:10021/"
}
data = json.dumps(data)
res = requests.post(url=url,data=data)