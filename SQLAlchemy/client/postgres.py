from SQLAlchemy.abstract.singleton import singleton
from SQLAlchemy.abstract.base import AbstractPostgreSqlClient


class PostgreSqlClient(AbstractPostgreSqlClient):
    """
    Do not restrict this class to be singleton because when application
    needs to connect to multiple databases of multiple resources.
    """
    def get_engine(self):
        return self.engine


@singleton
class PostgreSqlUnitTestClient(AbstractPostgreSqlClient):
    """
    To avoid creating redundant db engine randomly, return engine as the attribute of a singleton class
    """
    def get_engine(self):
        return self.engine
