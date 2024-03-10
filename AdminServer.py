from flask import Flask, Response, request ,jsonify
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
 
# @app.route("/GetManagerLeaderIP",methods =['GET'])
# def SendManagerLeaderIP():
#     data = {"leaderIP":"http://127.0.1.1:7021/"}
#     data = json.dumps(data)
#     return data


@app.route("/GetLeaderIPNode",methods =['POST'])
def sendLeaderIP():
    return getManagerLeader()


@app.route('/api/admin/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if username == 'a@a.com' and password == '123':
        token = 'login_done'
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
    



@app.route("/RequestOTP",methods =['GET'])
def SendOTP():
    otp = input("Enter Otp :")
    return jsonify(otp),200

@app.route("/HeartBeatFromManager",methods =['POST'])
def Updatemanager():
    req = request.data.decode()
    setManagerLeader(req["leaderIP"])
    return ("alive")


def build_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
def build_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


app.run(debug=False,port=3000,host='127.0.1.1')