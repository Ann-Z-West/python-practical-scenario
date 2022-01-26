from sqlalchemy.exc import SQLAlchemyError

from SQLAlchemy.client.postgres import PostgreSqlClient
from SQLAlchemy.database import with_media_factory, Student
from SQLAlchemy.database.sharing import docker_media_conn_uri, master_conn_uri

""" create media engines
docker_postgre_engine: db server running in docker container
local_postgre_engine: local db server
"""
# Import docker running db server connecting URI, using database test
docker_postgre_engine = PostgreSqlClient(docker_media_conn_uri, 'test').get_engine()
# Import local db server connecting URI, using database test2
local_postgre_engine = PostgreSqlClient(master_conn_uri, 'test2').get_engine()


def count_student(session):
    try:
        """
        count students
        """
        row_count = 0
        for instance in session.query(Student).order_by(Student.id):
            print(instance.name)
            row_count += 1
        session.commit()
        return row_count
    except SQLAlchemyError:
        raise


@with_media_factory(docker_postgre_engine)
def count_student_server_in_container(m_session):
    return count_student(m_session)


@with_media_factory(local_postgre_engine)
def count_student_local_server(m_session):
    return count_student(m_session)
