# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/admin/login', methods=['POST'])
def login():
    # Get username and password from the request
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Perform authentication logic
    if username == 'a@a.com' and password == '123':
        # Authentication successful
        # Generate and return a token
        token = 'login_done'
        return jsonify({'token': token}), 200
    else:
        # Authentication failed
        return jsonify({'error': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
