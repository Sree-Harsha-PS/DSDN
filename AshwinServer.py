from flask import Flask, Response, request
from flask_cors import CORS

global app
app = Flask(__name__)
CORS(app)

@app.route("/AddNode",methods =['POST'])
def Add_Node_to_Network():
    # seed
    # generateOpt
    # send Mail
    data = request.data.decode()
    print(data,type(data))
    return "success"



app.run(debug=False,port=5000,host='127.0.1.1')