#!/bin/env python3

from flask import Flask, request, make_response
from todo import TodoService
from json import loads


app = Flask(__name__)
svc = TodoService()


def cors_preflight():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response


@app.route('/api/todos', methods=['GET', 'POST', 'DELETE', 'OPTIONS'])
def todos():
    if request.method == 'GET':
        todos = svc.get_todos()
    if request.method == 'POST':
        todos = [svc.add_todo(loads(request.data)['text'])]
    elif request.method == 'DELETE':
        todos = [svc.del_todo(loads(request.data)['text'])]
    elif request.method == 'OPTIONS':
        return cors_preflight()

    response = make_response({'status': 'success', 'todos': todos}, 200)
    response.headers.add('Content-Type', 'application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    app.run('0.0.0.0')
