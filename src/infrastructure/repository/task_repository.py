from dataclasses import dataclass
from infrastructure.providers.postgres_provider import PostgresContextProvider
from sqlalchemy import Engine
from sqlmodel import select
from domain.task import Task


@dataclass
class TaskRepository:
    engine: Engine

    def add(self, task: Task):
        with PostgresContextProvider(self.engine) as session:
            if session is None:
                raise Exception("Could not connect to a database")
            else:
                session.add(task)

         