import os
from pathlib import Path

from sqlalchemy import create_engine, Select
from sqlalchemy.orm import Session
from sqlalchemy.orm import scoped_session, sessionmaker

from data_access.data_base import init_db


class BaseManager(object):
    def __init__(self, generate_example_data: bool = True):
        # Ensure the environment Variable is set
        db_file = os.environ.get('DB_FILE')
        if not db_file:
            raise ValueError("You have to define the environment variable 'DB_FILE'")
        self.__db_file = Path(db_file)

        # Ensure the db file exists, if not create a new db file with or without example data
        if not self.__db_file.is_file():
            init_db(db_file, generate_example_data=generate_example_data)

        # create the engine and the session.
        # the engine is private, no need for subclasses to be able to access it.
        self.__engine = create_engine(f'sqlite:///{db_file}')
        # create the session as db connection
        # subclasses need access, so every inheriting manager has access to this connection
        self._session = scoped_session(sessionmaker(bind=self.__engine))

    def select_all(self, query: Select):
        return self._session.execute(query).scalars().all()

    def select_one(self, query: Select):
        return self._session.execute(query).scalars().one()
