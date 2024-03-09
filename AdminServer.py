from flask import Flask, Response, request
from flask_cors import CORS

global app
app = Flask(__name__)
CORS(app)

@app.route("/GetManagerLeaderIP",methods =['POST'])
def SendManagerLeaderIP():
    return "http://127.0.0.1:7021/"

@app.route("/RequestOTP",methods =['GET'])
def SendOTP():
    otp = input("Enter Otp :")
    return str(otp)



app.run(debug=False,port=3000,host='127.0.1.1')