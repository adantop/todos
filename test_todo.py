import pytest
from datetime import datetime
from todo import TodoService

@pytest.fixture
def service():
    service = TodoService(test=True)
    service.add_todo("Study Python")
    yield service


def test_create_service():
    service = TodoService(test=True)
    assert isinstance(service, TodoService)
    assert isinstance(service.get_todos(), list)


def test_add_todo(service):
    text = "Build Website"
    todo = service.add_todo(text)
    assert isinstance(todo, dict)
    assert len(todo) == 2 and 'id' in todo and 'text' in todo
    assert todo['id']
    assert todo['text'] == text


def test_get_todos(service):
    todos = service.get_todos()
    assert isinstance(todos, list)
    assert len(todos) == 1


def test_get_todo(service):
    text = "Study Python"
    todo = service.get_todo(text)
    assert isinstance(todo, dict)
    assert 'id' in todo.keys()
    assert 'text' in todo.keys()
    assert todo['text'] == text


def test_del_todo(service):
    text = "Study Python"
    service.del_todo(text)
    assert service.get_todo(text) is None
