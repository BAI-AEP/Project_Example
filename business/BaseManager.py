import os
from pathlib import Path

from sqlalchemy import create_engine, Select
from sqlalchemy.orm import Session
from sqlalchemy.orm import scoped_session, sessionmaker

from data_access.data_base import init_db


class BaseManager(object):
    def __init__(self, generate_example_data: bool = True):
        db_file = os.environ.get('DB_FILE')
        if not db_file:
            raise ValueError("You have to define the environment variable 'DB_FILE'")
        self.__db_file = Path(db_file)
        if not self.__db_file.is_file():
            init_db(db_file, generate_example_data=generate_example_data)

        self.__engine = create_engine(f'sqlite:///{db_file}')
        self._session = scoped_session(sessionmaker(bind=self.__engine))

    @property
    def db_file(self):
        return self.__db_file

    @property
    def engine(self):
        return self.__engine

    @property
    def session(self):
        return self._session

    def select_all(self, query: Select):
        return self._session.execute(query).scalars().all()

    def select_one(self, query: Select):
        return self._session.execute(query).scalars().one()
