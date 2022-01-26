from contextlib import contextmanager

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import scoped_session, sessionmaker

from SQLAlchemy.client.postgres import PostgreSqlClient

# local Postgre server with port 5432
master_conn_uri = "postgresql://localhost/"
# Postgre Server running in docker container with # port 5433
docker_media_conn_uri = "postgresql://postgres@localhost:5433/"

pool_timeout = 3600  # in seconds

master_engine = PostgreSqlClient(master_conn_uri, 'test').get_engine()
db_master_session = scoped_session(sessionmaker(bind=master_engine))
session = db_master_session()


@contextmanager
def session_maker():
    try:
        yield session
        session.commit()
    except SQLAlchemyError:
        session.rollback()
    finally:
        session.close()


"""
Design pattern for two scenarios: 
    1. databases in master-media structure 
    2. requires switching db sources
This is a double layered enclosure function to decorate a passed in fn, 
which enables passing in media_engine as parameter
"""


def with_media_factory(media_engine):
    def with_media(fn):
        def go(*args, **kwargs):
            old_bind = session.bind
            session.bind = media_engine
            try:
                media_session = session
                return fn(media_session, *args, **kwargs)
            except SQLAlchemyError:
                session.rollback()
                raise
            finally:
                session.bind = old_bind
                session.close()
        return go
    return with_media
