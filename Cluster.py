from pyraft import raft
import threading
from time import sleep
import requests
import json
from flask import Flask, Response, request
from flask_cors import CORS
import networkx as nx

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

global app
app = Flask(__name__)
CORS(app)

matrix=[[0,1,5,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],[1,0,6,3,0,0,0,0,0,0,0,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[5,6,0,0,9,5,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,3,0,0,0,8,0,0,0,0,5,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,9,0,0,0,4,0,0,8,10,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0],[0,0,5,8,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,7,0,4,4,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,4,0,6,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,8,0,0,0,0],[0,0,0,0,8,0,5,0,6,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0],[0,0,0,5,10,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0],[8,11,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,7,0,0,0,0,0,0,0,0,0],[0,0,0,7,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,4,0,5,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,4,0,0,0,0],[0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,5,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,2,0,8,0,0,0,0,3,0,0,0,6,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,8,0,0,0,0,0,0,3,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,3],[0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,5,0,3,4,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,3,0,2,0,0,0,0,0,0,0],[0,0,0,0,7,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,4,2,0,0,0,2,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,3,0,0,0,0,0,0,4,3,0,4,0],[0,0,0,0,0,0,0,0,8,6,0,0,0,0,4,0,0,0,0,0,0,0,2,0,4,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,7,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,7,0,0],[7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0]]


# To find next path
# def find_next_node(source,destination):
#     p=nx.shortest_path(matrix,source,destination,weight='weight')
#     return p[1]
# print(find_next_node(1,18))

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
                },
                "4":{
                    "IP":"http://127.0.1.1:10004/",
                    "Status":"dead"
                },
                "5":{
                    "IP":"http://127.0.1.1:10005/",
                    "Status":"dead"
                },
                "6":{
                    "IP":"http://127.0.1.1:10006/",
                    "Status":"dead"
                },
                "7":{
                    "IP":"http://127.0.1.1:10007/",
                    "Status":"dead"
                },
                "8":{
                    "IP":"http://127.0.1.1:10008/",
                    "Status":"dead"
                },
                "9":{
                    "IP":"http://127.0.1.1:10009/",
                    "Status":"dead"
                },
                "10":{
                    "IP":"http://127.0.1.1:10010/",
                    "Status":"dead"
                },
                "11":{
                    "IP":"http://127.0.1.1:10011/",
                    "Status":"dead"
                },
                "12":{
                    "IP":"http://127.0.1.1:10012/",
                    "Status":"dead"
                },
                "13":{
                    "IP":"http://127.0.1.1:10013/",
                    "Status":"dead"
                },
                "14":{
                    "IP":"http://127.0.1.1:10014/",
                    "Status":"dead"
                },
                "15":{
                    "IP":"http://127.0.1.1:10015/",
                    "Status":"dead"
                },
                "16":{
                    "IP":"http://127.0.1.1:10016/",
                    "Status":"dead"
                },
                "17":{
                    "IP":"http://127.0.1.1:10017/",
                    "Status":"dead"
                },
                "18":{
                    "IP":"http://127.0.1.1:10018/",
                    "Status":"dead"
                },
                "19":{
                    "IP":"http://127.0.1.1:10019/",
                    "Status":"dead"
                },
                "20":{
                    "IP":"http://127.0.1.1:10020/",
                    "Status":"dead"
                },
                "21":{
                    "IP":"http://127.0.1.1:10021/",
                    "Status":"dead"
                },
                "22":{
                    "IP":"http://127.0.1.1:10022/",
                    "Status":"dead"
                },
                "23":{
                    "IP":"http://127.0.1.1:10023/",
                    "Status":"dead"
                },
                "24":{
                    "IP":"http://127.0.1.1:10024/",
                    "Status":"dead"
                },
                "25":{
                    "IP":"http://127.0.1.1:10025/",
                    "Status":"dead"
                },
                "26":{
                    "IP":"http://127.0.1.1:10026/",
                    "Status":"dead"
                },
                "27":{
                    "IP":"http://127.0.1.1:10027/",
                    "Status":"dead"
                },
                "28":{
                    "IP":"http://127.0.1.1:10028/",
                    "Status":"dead"
                },
                "29":{
                    "IP":"http://127.0.1.1:10029/",
                    "Status":"dead"
                },
                "30":{
                    "IP":"http://127.0.1.1:10030/",
                    "Status":"dead"
                }
            }
ClusterMangerIP = "" 
matrix = []

def getmatrix():
    global matrix
    return matrix
def setmatrix(m):
    global matrix
    matrix = m
    return matrix

def stringToMatrix(data):
    matrix =[]
    data = str(data[2:-2])
    data = data.replace(" ","")
    data = data.replace("[","")
    data = data.replace("],","|")
    matrix = data.split("|")
    for i in range(len(matrix)):
        matrixtring = matrix[i].split(",")
        matrix[i] = []
        for c in matrixtring:

            try:
                c = int(c)
            except:
                pass    
            matrix[i].append(c)
                
    return matrix   

def add_node(matrix, new_node, connections):
    
    matrix.insert(new_node, [0] * len(matrix))
    for row in matrix:
        row.insert(new_node, 0)


    for connection, weight in connections:
        matrix[new_node - 1][connection - 1] = weight  
        matrix[connection - 1][new_node - 1] = weight

    return matrix

def setClusterManagerIP(ip):
    global ClusterMangerIP
    ClusterMangerIP = ip
    return ClusterMangerIP

def getClusterManagerIP():
    global ClusterMangerIP
    return ClusterMangerIP

def minDistance(dist, visited):
    min_dist = float("inf")
    min_index = -1
    for v in range(len(dist)):
        if dist[v] < min_dist and not visited[v]:
            min_dist = dist[v]
            min_index = v
            sleep(min_index*0.002)
    return min_index

def dijkstra(graph, src, dest):
    V = len(graph)
    dist = [float("inf")] * V
    dist[src-1] = 0
    visited = [False] * V
    previous_nodes = [-1] * V
    
    for i in range(V):
        u = minDistance(dist, visited)
        visited[u] = True

        for v in range(V):
            if graph[u][v] > 0 and not visited[v] and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
                previous_nodes[v] = u
    path = []
    current = dest - 1
    while current != -1:
        path.append(current + 1)
        # sleep()
        current = previous_nodes[current]

    path.reverse()
    print(path)
    # sleep(1)
    # print(dist[dest-1])
    return path[1]

# x=dijkstra(matrix, 1, 6)
# print(x)

# x=dijkstra(matrix, 3, 7)
# print(x)


@app.route("/",methods =["POST"])
def Add_Node_to_Network():

    data = request.data.decode()
    # print(data,type(data))
    return "success"

@app.route("/SendNextNode",methods =['POST'])
def RequestFromNode():
    print("recived")
    data = request.data.decode()
    print(data)
    requests.post(getClusterManagerIP()+"ReciveNodeIP",data=data)
    return "alive"

@app.route("/ComputeShortestPath",methods =['POST'])
def shortestpath():
    req = request.data.decode()
    data = json.loads(req)
    # print(data["Source"])    
    # print(data["Destination"]) 
    sourceID =   int(data["Current"].split(":")[-1][1:-1])
    destinationID =   int(data["Destination"].split(":")[-1][1:-1])
    id = dijkstra(getmatrix(),sourceID,destinationID)
    print(sourceID,destinationID,id)
    urlPort = 10000+id
    print("next==========?",id)
    url = "http://127.0.1.1:"+str(urlPort)+"/GetNextNode"
    print(url)
    res = requests.post(url=url,data=req) 
    try:
        print("sent")
    except:
        print("not able to send================>")    
    return ""

@app.route("/HeartBeatFromManager",methods =['POST'])
def heartBeatFromManager():

    data = request.data.decode()
    data = json.loads(data)
    # print(data,type(data))
    # global ClusterMangerIP
    # ClusterMangerIP = data["leaderIP"]
    setClusterManagerIP(data["leaderIP"])
    matrix = stringToMatrix(data["matrix"])
    setmatrix(matrix)
    # global NodesIP
    # NodesIP = data["NodesIP"]
    
    # print(getClusterManagerIP())
    
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

