import requests
import json
url = "http://127.0.0.1:5021/SendNextNode"
data = {
    "Source":"http://127.0.0.1:10001/",
    "Destination":"http://127.0.0.1:10003/"
}
data = json.dumps(data)
res = requests.post(url=url,data=data)