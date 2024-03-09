from pyraft import raft
import threading
from time import sleep

from flask import Flask, Response, request
from flask_cors import CORS

global app
app = Flask(__name__)
CORS(app)

@app.route("/",methods =['POST'])
def Add_Node_to_Network():

    data = request.data.decode()
    print(data,type(data))
    return "success"



def clusterLeader(node):
    while not node.shutdown_flag:
        if(node.state == 'l'):
            print(node.state)
            sleep(3)
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
x4 = threading.Thread(target=start_server)
x4.start()


node.worker.handler['on_leader'] = clusterLeaderCallback
node.worker.handler['on_follower'] = clusterFollowerCallback

node.start()
node.join()