from flask import Flask, Response, request
from flask_cors import CORS
import json

global app
app = Flask(__name__)
CORS(app)
 
managerLeaderIP = "" 

def setManagerLeader(data):
    global managerLeaderIP
    managerLeaderIP = data
    return managerLeaderIP
def getManagerLeader():
    global managerLeaderIP
    return managerLeaderIP
 
@app.route("/GetManagerLeaderIP",methods =['GET'])
def SendManagerLeaderIP():
    data = {"leaderIP":"http://127.0.1.1:7021/"}
    data = json.dumps(data)
    return data




@app.route("/RequestOTP",methods =['GET'])
def SendOTP():
    otp = input("Enter Otp :")
    return str(otp)

@app.route("/HeartBeatFromManager",methods =['POST'])
def Updatemanager():
    req = request.data.decode()
    setManagerLeader(req["leaderIP"])
    return "alive"



app.run(debug=False,port=3000,host='127.0.1.1')