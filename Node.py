Id = int(input("Enter the Node ID: "))
port = 10000+Id


from flask import Flask, Response, request
from flask_cors import CORS
import requests
import json
import threading
import time


global app
app = Flask(__name__)
CORS(app)
leaderIP =""
def setLeaderIP(ip):
    global leaderIP 
    leaderIP = ip
    return leaderIP
def getLeaderIP():
    global leaderIP
    return leaderIP
@app.route("/NodeHeartBeats",methods =['POST'])
def HeartBeatStatus():
    setLeaderIP(request.data.decode())
    print("recieved IP")
    return "alive"

@app.route("/GetNextNode",methods =['POST'])
def getNextNode():
    req = request.data.decode()
    # data = json.loads(req)
    url = leaderIP+"SendNextNode"
    # print(url,data)
    res=requests.post(url=url,data=req)
    # print(res)
    return "alive"


# def LeaderIpDecode():
#     url = getLeaderIP()
#     # data = {
#     #             "Source":"http://127.0.1.1:"+str(port),
#     #             "Destination":"http://127.0.1.1:"+str(port2)
#     #         }
#     data = json.dumps(data)
#     return res

def start_server():
        app.run(debug=False,port=port,host='127.0.1.1')
startServer = threading.Thread(target=start_server)
startServer.start()
# time.sleep(10)
# LeaderIpDecode()    