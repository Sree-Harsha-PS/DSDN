from pyraft import raft
import threading
from time import sleep
import requests

from flask import Flask, Response, request
from flask_cors import CORS

global app
app = Flask(__name__)
CORS(app)
matrix = []

NodesIP = ["http://127.0.1.1:10001/","http://127.0.1.1:10002/","http://127.0.1.1:10003/","http://127.0.1.1:10004/","http://127.0.1.1:10005/","http://127.0.1.1:10006/","http://127.0.1.1:10007/","http://127.0.1.1:10008/","http://127.0.1.1:10009/","http://127.0.1.1:10010/","http://127.0.1.1:10011/","http://127.0.1.1:10012/","http://127.0.1.1:10013/","http://127.0.1.1:10014/","http://127.0.1.1:10015/","http://127.0.1.1:10016/","http://127.0.1.1:10017/","http://127.0.1.1:10018/","http://127.0.1.1:10019/","http://127.0.1.1:10020/","http://127.0.1.1:10021/","http://127.0.1.1:10022/","http://127.0.1.1:10023/","http://127.0.1.1:10024/","http://127.0.1.1:10025/","http://127.0.1.1:10026/","http://127.0.1.1:10027/","http://127.0.1.1:10028/","http://127.0.1.1:10029/","http://127.0.1.1:10030/"]
NodeDetails = {
                "1" :{
                    "IP":"http://127.0.1.1:10001/",
                    "Status":"dead",
                },
                "2":{
                    "IP":"http://127.0.1.1:10002/",
                    "Status":"dead"
                },
                "3":{
                    "IP":"http://127.0.1.1:10003/",
                    "Status":"dead"
                }
                # "4":{
                #     "IP":"http://127.0.1.1:10004/",
                #     "Status":"dead"
                # },
                # "5":{
                #     "IP":"http://127.0.1.1:10005/",
                #     "Status":"dead"
                # },
                # "6":{
                #     "IP":"http://127.0.1.1:10006/",
                #     "Status":"dead"
                # },
                # "7":{
                #     "IP":"http://127.0.1.1:10007/",
                #     "Status":"dead"
                # },
                # "8":{
                #     "IP":"http://127.0.1.1:10008/",
                #     "Status":"dead"
                # },
                # "9":{
                #     "IP":"http://127.0.1.1:10009/",
                #     "Status":"dead"
                # },
                # "10":{
                #     "IP":"http://127.0.1.1:10010/",
                #     "Status":"dead"
                # },
                # "11":{
                #     "IP":"http://127.0.1.1:10011/",
                #     "Status":"dead"
                # },
                # "12":{
                #     "IP":"http://127.0.1.1:10012/",
                #     "Status":"dead"
                # },
                # "13":{
                #     "IP":"http://127.0.1.1:10013/",
                #     "Status":"dead"
                # },
                # "14":{
                #     "IP":"http://127.0.1.1:10014/",
                #     "Status":"dead"
                # },
                # "15":{
                #     "IP":"http://127.0.1.1:10015/",
                #     "Status":"dead"
                # },
                # "16":{
                #     "IP":"http://127.0.1.1:10016/",
                #     "Status":"dead"
                # },
                # "17":{
                #     "IP":"http://127.0.1.1:10017/",
                #     "Status":"dead"
                # },
                # "18":{
                #     "IP":"http://127.0.1.1:10018/",
                #     "Status":"dead"
                # },
                # "19":{
                #     "IP":"http://127.0.1.1:10019/",
                #     "Status":"dead"
                # },
                # "20":{
                #     "IP":"http://127.0.1.1:10020/",
                #     "Status":"dead"
                # },
                # "21":{
                #     "IP":"http://127.0.1.1:10021/",
                #     "Status":"dead"
                # },
                # "22":{
                #     "IP":"http://127.0.1.1:10022/",
                #     "Status":"dead"
                # },
                # "23":{
                #     "IP":"http://127.0.1.1:10023/",
                #     "Status":"dead"
                # },
                # "24":{
                #     "IP":"http://127.0.1.1:10024/",
                #     "Status":"dead"
                # },
                # "25":{
                #     "IP":"http://127.0.1.1:10025/",
                #     "Status":"dead"
                # },
                # "26":{
                #     "IP":"http://127.0.1.1:10026/",
                #     "Status":"dead"
                # },
                # "27":{
                #     "IP":"http://127.0.1.1:10027/",
                #     "Status":"dead"
                # },
                # "28":{
                #     "IP":"http://127.0.1.1:10028/",
                #     "Status":"dead"
                # },
                # "29":{
                #     "IP":"http://127.0.1.1:10029/",
                #     "Status":"dead"
                # },
                # "30":{
                #     "IP":"http://127.0.1.1:10030/",
                #     "Status":"dead"
                # }
            }
ClusterMangerIP = "" 


@app.route("/",methods =["POST"])
def Add_Node_to_Network():

    data = request.data.decode()
    print(data,type(data))
    return "success"

@app.route("/SendNextNode",methods =['POST'])
def RequestFromNode():
    print("recived")
    data = request.data.decode()
    print(data)
    return "alive"

@app.route("/HeartBeatFromManager",methods =['get'])
def heartBeatFromManager():

    data = request.data.decode()
    print(data,type(data))
    global ClusterMangerIP
    ClusterMangerIP = data
    
    return "alive"


def SendHeartBeatToNodes():
    for Node in NodeDetails:
        try:
            data = bytes("http://127.0.1.1:"+str(node.port+1)+'/','ascii')
            NodeDetails[Node]["Status"]= "alive"
            res = requests.post(NodeDetails[Node]["IP"]+"NodeHeartBeats",data=data)
            # print(NodeDetails[Node]["IP"]+"NodeHeartBeats")
            # NodeDetails[IP] = "alive"
        except:
            NodeDetails[Node]["Status"]= "dead"
            # NodeStatus[IP] = "dead"
        # print(NodeDetails[Node]["Status"],Node)

def clusterLeader(node):
    while not node.shutdown_flag:
        if(node.state == 'l'):
            print(node.port)
            SendHeartBeatToNodes()
            # print(node.state)
            # print(NodeStatus)
            # sleep(3)
def clusterFollower(node):
    while not node.shutdown_flag:
        if(node.state == 'f'):
            print(node.state)
            sleep(3)

def clusterLeaderCallback(node):
    print("cluster leader")
    node = threading.Thread(target=clusterLeader, args=(node,))
    node.start()
def clusterFollowerCallback(node):
    print("cluster follower")
    node = threading.Thread(target=clusterFollower, args=(node,))
    node.start()

node = raft.make_default_node()
port = int(node.port)+1
def start_server():
        app.run(debug=False,port=port,host='127.0.1.1')
startServer = threading.Thread(target=start_server)
startServer.start()


node.worker.handler['on_leader'] = clusterLeaderCallback
node.worker.handler['on_follower'] = clusterFollowerCallback

node.start()
node.join()

