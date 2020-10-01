#!/bin/env python3

import uuid


class TodoService:
    todos = [
        {'id': uuid.uuid1(), 'text': 'Study Python'}
    ]

    def get_todos(self) -> list:
        return self.todos
    
    def get_todo(self, todo: str) -> dict:
        filtered = [t for t in self.todos if t['text'] == todo]
        return filtered.pop() if filtered else None
    
    def add_todo(self, todo: str) -> dict:
        if self.get_todo(todo):
            raise ValueError(f'todo "{todo}" already exist')

        todo = {'id': uuid.uuid1(), 'text': todo}
        self.todos.append(todo)
        return todo
    
    def del_todo(self, todo: str) -> dict:
        todo = self.get_todo(todo)
        if todo:
            self.todos.remove(todo)
        return todo
