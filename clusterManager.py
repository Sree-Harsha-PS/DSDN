from pyraft import raft
import threading
from time import sleep
import requests
import  json

import smtplib
from flask import Flask, Response, request
from flask_cors import CORS

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

import pyotp
clusterIP = ['http://127.0.1.1:5011/','http://127.0.1.1:5021/','http://127.0.1.1:5031/']
clusterStatus = {
                    'http://127.0.1.1:5011/':"dead",
                    'http://127.0.1.1:5021/':"dead",
                    'http://127.0.1.1:5031/':"dead",
                }

matrix=[[0,1,5,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7],[1,0,6,3,0,0,0,0,0,0,0,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[5,6,0,0,9,5,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,3,0,0,0,8,0,0,0,0,5,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,9,0,0,0,4,0,0,8,10,0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0],[0,0,5,8,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,7,0,4,4,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,4,0,6,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,8,0,0,0,0],[0,0,0,0,8,0,5,0,6,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0],[0,0,0,5,10,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0],[8,11,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,7,0,0,0,0,0,0,0,0,0],[0,0,0,7,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,4,0,5,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,4,0,0,0,0],[0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,5,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,2,0,8,0,0,0,0,3,0,0,0,6,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,0,8,0,0,0,0,0,0,3,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,3],[0,0,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,5,0,3,4,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,3,0,2,0,0,0,0,0,0,0],[0,0,0,0,7,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,4,2,0,0,0,2,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,3,0,0,0,0,0,0,4,3,0,4,0],[0,0,0,0,0,0,0,0,8,6,0,0,0,0,4,0,0,0,0,0,0,0,2,0,4,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,0,0,0,0,0,0,0,0,0,0,7,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,7,0,0],[7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0]]
NodesIP = ["http://127.0.1.1:10001/","http://127.0.1.1:10002/","http://127.0.1.1:10003/","http://127.0.1.1:10004/","http://127.0.1.1:10005/","http://127.0.1.1:10006/","http://127.0.1.1:10007/","http://127.0.1.1:10008/","http://127.0.1.1:10009/","http://127.0.1.1:10010/","http://127.0.1.1:10011/","http://127.0.1.1:10012/","http://127.0.1.1:10013/","http://127.0.1.1:10014/","http://127.0.1.1:10015/","http://127.0.1.1:10016/","http://127.0.1.1:10017/","http://127.0.1.1:10018/","http://127.0.1.1:10019/","http://127.0.1.1:10020/","http://127.0.1.1:10021/","http://127.0.1.1:10022/","http://127.0.1.1:10023/","http://127.0.1.1:10024/","http://127.0.1.1:10025/","http://127.0.1.1:10026/","http://127.0.1.1:10027/","http://127.0.1.1:10028/","http://127.0.1.1:10029/","http://127.0.1.1:10030/"]

LeaderStatus = "dead"


global app
app = Flask(__name__)
CORS(app)

def setLeaderStatus(data):
    global LeaderStatus 
    LeaderStatus = data
    return LeaderStatus

def getLeaderStatus():
    global LeaderStatus
    return LeaderStatus
    

def generate_otp():
    key="DuckSquadDontNap"
    totp=pyotp.TOTP(key, interval=120)
    return totp.now()


def sendMail(totp, subject):
    try:
        subject = 'One-time Password'
        YOUR_GOOGLE_EMAIL = 'ashwintest03@gmail.com'
        YOUR_GOOGLE_EMAIL_APP_PASSWORD = 'iwyv wdwi zcmr ljxu'  
        smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtpserver.ehlo()
        smtpserver.login(YOUR_GOOGLE_EMAIL, YOUR_GOOGLE_EMAIL_APP_PASSWORD)
        sent_from = YOUR_GOOGLE_EMAIL
        sent_to = 'balajiagmohan@gmail.com'
        email_text = "Subject: {}\n\nThe OTP is\n{}".format(subject, str(totp))
        smtpserver.sendmail(sent_from, sent_to, email_text)
        smtpserver.close()
        return "successful"
    except:
        return "failed"



AddNodeVotes = 0
LogNo = -1
idx = -1

def incrementIdx():
    global idx
    idx = (idx+1) % len(clusterIP)

def ResetAddNodeVotes():
    global AddNodeVotes
    AddNodeVotes = 0
    return AddNodeVotes
def GetAddNodeVotes():
    global AddNodeVotes
    return AddNodeVotes
def updateAddNodeVotes(votes):
    global AddNodeVotes
    AddNodeVotes += votes 

def GetLogNo():
    global LogNo
    return LogNo
def incrementLogNo():
    global LogNo
    LogNo += 1
    return LogNo

def delete(node):
    global matrix
    del matrix[node-1]
    for row in matrix:
        del row[node-1]
    return matrix


def add_node(new_node, connections):
    global matrix
    matrix.insert(new_node, [0] * len(matrix))
    for row in matrix:
        row.insert(new_node, 0)


    for connection, weight in connections:
        matrix[new_node - 1][connection - 1] = weight  
        matrix[connection - 1][new_node - 1] = weight

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

def followersAddNodeRequest(data):
    print(node.port)
    # print(node.peers[1].port)
    votes = 0 
    for peer in node.peers.values():
        url = 'http://127.0.1.1:'+str(int(peer.port)+1)+'/FollowerAddNode'
        try:
            res = requests.post(url=url,data=data)
            print(res.content.decode())
            votes +=1
        except:
            print("failed to add")  
    return votes

@app.route("/FollowerAddNode",methods =['POST'])
async def  addNodeToNetwork():
    print(request.data.decode())
    data,LeaderLogNo = request.data.decode().split("|")
    print(data,LeaderLogNo)
    incrementLogNo()
    if int(LeaderLogNo) >= LogNo:
        # update in main memory
        file = open(f"Cluster_Manager{node.nid}_log.txt","+a")
        file.write(f"log {LeaderLogNo}({node.state}): Node {0} is added to the network\n")
        file.close()
        data = {
                "id":"31",
                "list":"[[7,4],[28,1],[12,5]]"
               }
        data = json.dumps(data)
        data = json.loads(data)
        list = data["list"]
        list = stringToMatrix(list)
        add_node(int(data["id"]),list)
        return "Sucessfully added"
    else:
        return "Log ahead"



@app.route("/ReciveNodeIP",methods =['POST'])
def  ReciveNodeIP():
    req = request.data.decode()
    print(req)
    incrementIdx()
    while(clusterStatus[clusterIP[idx]] == "dead"):
        print(clusterIP[idx]+"ComputeShortestPath")
    requests.post(clusterIP[idx]+"ComputeShortestPath",req)
    
    
    

@app.route("/GetOTPFromAdmin",methods =['GET'])
def  GetOtp():
    # otp = generate_otp()
    noOfNodes = 3
    AdminOTP = request.data.decode()
    data = request.data.decode()+"|"+str(LogNo+1)
    if(AdminOTP == generate_otp()):
    
        updateAddNodeVotes(followersAddNodeRequest(data)+1)
        print(AddNodeVotes + 1)
        incrementLogNo()
        if(GetAddNodeVotes() > noOfNodes//2):
            # update in main memory 
            file = open(f"Cluster_Manager{node.nid}_log.txt","+a")
            file.write(f"log {GetLogNo()}({node.state}): Node {0} is added to the network\n")
            file.close()
            data = {
                "id":"31",
                "list":"[[7,4],[28,1],[12,5]]"
               }
            data = json.dumps(data)
            data = json.loads(data)
            list = data["list"]
            list = stringToMatrix(list)
            add_node(int(data["id"]),list)
            ResetAddNodeVotes()
            return "success"
        else:
            file = open(f"Cluster_Manager{node.nid}_log.txt","+a")
            file.write(f"log {GetLogNo()}({node.state}): Failed to Node {0} to the network\n")
            file.close()        
            ResetAddNodeVotes()
            return "failed"
    else:
        incrementLogNo()
        file = open(f"Cluster_Manager{node.nid}_log.txt","+a")
        file.write(f"Login attempt failed from admin\n")
        file.close()
        return "Wrong OTP"    
    
@app.route("/AddNode",methods =['POST'])
def  Add_Node_to_Network():
    otp = generate_otp()
    sendMail(otp)   
    return "Otp Sent"
    


# @app.route("/",methods =['POST'])
def sendHeartBeatToClusters():
    for IP in clusterIP:
        try:
            data = {
                "leaderIP":"http://127.0.1.1:"+str(node.port+1)+'/',
                "matrix" : str(matrix),
                "NodesIP" : str(NodesIP)
            }
            data = json.dumps(data)
            # "http://127.0.1.1:"+str(node.port+1)
            res = requests.post(url=IP+"HeartBeatFromManager",data=data)
            clusterStatus[IP] = "alive"
            # print(res.content.decode())
        except:
            # print("error madu",IP)    
            clusterStatus[IP] = "dead"
        # print(IP)

def sendIPToAdmin():
    try:
        data = {"leaderIP":"http://127.0.1.1:"+str(node.port+1)+'/'}
        data = json.dumps(data)
        res = requests.post("http://127.0.1.1:3000/HeartBeatFromManager",data=data)
        setLeaderStatus("alive")
    except:
        setLeaderStatus("dead")
        pass
        

def  clusterManagerLeader(node):
    while not node.shutdown_flag:
        if(node.state == 'l'):
            print(node.state)
            sendHeartBeatToClusters()
            print(clusterStatus)
            sleep(3)
def  clusterManagerFollower(node):
    while not node.shutdown_flag:
        if(node.state == 'f'):
            print(node.state)
            sleep(3)

def  clusterManagerLeaderCallback(node):
    print("clusterManager leader")
    node = threading.Thread(target=clusterManagerLeader, args=(node,))
    node.start()
def clusterManagerFollowerCallback(node):
    print("clusterManager follower")
    node = threading.Thread(target=clusterManagerFollower, args=(node,))
    node.start()

node = raft.make_default_node()
port = int(node.port)+1
def start_server():
        app.run(debug=False,port=port,host='127.0.1.1')
startHTTPServer = threading.Thread(target=start_server)
startHTTPServer.start()


node.worker.handler['on_leader'] = clusterManagerLeaderCallback
node.worker.handler['on_follower'] = clusterManagerFollowerCallback

node.start()
node.join()