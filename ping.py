from cmath import pi
import os
import requests
import time

from flask import Flask, jsonify, request 
from flask_httpauth import HTTPDigestAuth as FlaskDigestAuth


#https://pinghcb.herokuapp.com/
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret key here'
auth = FlaskDigestAuth()

users = {
    "vcu":"rams"
    }

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/ping', methods=['GET'])
@auth.login_required
def index():
    
    response = requests.get(url='http://127.0.0.1:5000/pong')
    return jsonify({
        'pingpong_t': str(response.elapsed.total_seconds()*1000)
    }),201

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5001,debug=True)
