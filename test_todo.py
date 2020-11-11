
from todo import TodoService
from datetime import datetime

url = 'sqlite:///:memory:'

def test_create_service():
    svc = TodoService(url)
    assert isinstance(svc, TodoService)
    assert isinstance(svc.get_todos(), list)


def test_add_todo():
    svc = TodoService(url)
    text = "Build Website"
    todo = svc.add_todo(text)
    assert isinstance(todo, dict)
    assert len(todo) == 2 and 'id' in todo and 'text' in todo
    assert todo['id']
    assert todo['text'] == text


def test_get_todos():
    svc = TodoService(url)
    svc.add_todo("Build Website")
    todos = svc.get_todos()
    assert isinstance(todos, list)
    assert len(todos) == 1


def test_get_todo():
    svc = TodoService(url)
    text = "Build Website"
    svc.add_todo(text)
    todo = svc.get_todo(text)
    assert isinstance(todo, dict)
    assert 'id' in todo.keys()
    assert 'text' in todo.keys()
    assert todo['text'] == text


def test_del_todo():
    svc = TodoService(url)
    text = "Build Website"
    _ = svc.add_todo(text)
    svc.del_todo(text)
    assert svc.get_todo(text) is None
