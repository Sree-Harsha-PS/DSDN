from flask import Flask, Response, request
from flask_cors import CORS

global app
app = Flask(__name__)
CORS(app)

@app.route("/GetManagerLeaderIP",methods =['POST'])
def Add_Node_to_Network():
    return "http://127.0.1.1:7021/"


app.run(debug=False,port=5000,host='127.0.1.1')