import uuid
import json
import os
from yaml import safe_load
from collections.abc import Iterable
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


class Todo(declarative_base()):
    __tablename__ = "todo"

    id = Column("id", String(37), primary_key=True)
    text = Column("text", String(255), unique=True)

    def __repr__(self):
        return f"Todo('{self.id}', '{self.text}')"

    def to_dict(self):
        return dict(id=self.id, text=self.text)


class TodoService:

    def __init__(self, test: bool = False):
        url = self._url(test)
        self.engine = create_engine(url, echo=True, pool_recycle=3600)
        Todo.metadata.create_all(bind=self.engine)
        self.session = sessionmaker(bind=self.engine)()

    def get_todos(self) -> list:
        return [e.to_dict() for e in self.session.query(Todo).all()]

    def get_todo(self, text: str) -> dict:
        todo = self.session.query(Todo).filter_by(text=text).first()
        if todo:
            return todo.to_dict()

    def add_todo(self, text: str) -> dict:
        todo = Todo(id=str(uuid.uuid1()), text=text)
        self.session.add(todo)
        self.session.commit()
        return todo.to_dict()

    def del_todo(self, text: str) -> dict:
        todo = self.session.query(Todo).filter_by(text=text).first()
        self.session.delete(todo)
        self.session.commit()

    def _url(self, test: bool):
        if test:
            return 'sqlite:///:memory:'
        else:
            url = 'mysql+pymysql://{db[user]}:{db[password]}@{db[host]}/{db[database]}'
            db = safe_load(
                open(os.path.join(os.path.dirname(__file__), "db.yaml")))
            return url.format(db=db)


def main():
    svc = TodoService()

    for todo in svc.get_todos():
        print(json.dumps(todo))


if __name__ == '__main__':
    main()
