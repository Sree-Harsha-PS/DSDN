import requests
import json
import time
import threading
url = "http://127.0.1.1:10001/GetNextNode"
data = {
    "Source":"http://127.0.1.1:10001/",
    "Current":"http://127.0.1.1:10001/",
    "Destination":"http://127.0.1.1:10006/"
}
data = json.dumps(data)
start = time.time()
def route1(): 
    res = requests.post(url=url,data=data)
def route1(): 
    res = requests.post(url=url,data=data)
def route1(): 
    res = requests.post(url=url,data=data)

t1 = threading.Thread(target = route1)
t2 = threading.Thread(target = route1)
t3 = threading.Thread(target = route1)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

end = time.time()

print(end-start)