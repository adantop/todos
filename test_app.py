#!/usr/bin/python3

import app
import json
import re
import pytest


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client


def test_cors_preflight(client):
    rv = client.options('/api/todos')
    assert 'Access-Control-Allow-Origin'  in rv.headers
    assert 'Access-Control-Allow-Headers' in rv.headers
    assert 'Access-Control-Allow-Methods' in rv.headers


def test_get_todos(client):
    rv = client.get('/api/todos')
    data = json.loads(rv.data)
    assert rv.status_code == 200
    assert isinstance(data, dict)
    assert 'status' in data and 'todos' in data
    assert rv.headers['Content-Type'] == 'application/json'
    assert 'Access-Control-Allow-Origin' in rv.headers
