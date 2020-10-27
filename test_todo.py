#!/usr/bin/python3

from todo import TodoService


def test_create_service():
    todo_service = TodoService()
    assert isinstance(todo_service, TodoService)
    assert isinstance(todo_service.todos, list)


def test_get_todos():
    todo_service = TodoService()
    todos = todo_service.get_todos()
    assert isinstance(todos, list)
    assert len(todos) == 1


def test_get_todo():
    todo_service = TodoService()
    todo_text = todo_service.todos[0]['text']
    todo = todo_service.get_todo(todo_text)
    assert isinstance(todo, dict)
    assert 'id' in todo.keys()
    assert 'text' in todo.keys()
    assert todo['text'] == todo_text


def test_add_todo():
    todo_service = TodoService()
    todo_text = 'Build Website'
    todo = todo_service.add_todo(todo_text)
    assert isinstance(todo, dict)
    assert len(todo) == 2 and 'id' in todo and 'text' in todo
    assert todo['id']
    assert todo['text'] == todo_text


def test_del_todo():
    todo_service = TodoService()
    todo_text = 'Build Backend'
    todo_added = todo_service.add_todo(todo_text)
    len_added = len(todo_service.todos)
    todo_deleted = todo_service.del_todo(todo_text)
    assert todo_added is todo_deleted
    assert len(todo_service.todos) == len_added - 1
    assert todo_service.get_todo(todo_text) is None
