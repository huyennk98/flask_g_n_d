from flask import Flask
from flask import request, jsonify
from random import sample

server = Flask(__name__)


@server.route('/test', methods=['GET'])
def print_hi():
    # Use a breakpoint in the code line below to debug your script.

    request_data = request.get_json(force=True)

    return request_data

# @server.route('/')
# def hello_world():
#     return 'hello world!'

# def run_request():
#     index = int(request.json['index'])
#     list = ['red', 'green', 'blue', 'yellow', 'black']
#     return list[index]
# 
# @server.route('/', methods=['GET', 'POST'])
# def hello_world():
#     if request.method == 'GET':
#         return 'The model is up and running. Send a POST request'
#     else:
#         return run_request()
