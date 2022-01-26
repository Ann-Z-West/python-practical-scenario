import abc

import sqlalchemy

"""
This is an abstract class to restrict the behavior of concrete classes that inherited from it
"""


class AbstractPostgreSqlClient:
    __metaclass__ = abc.ABCMeta

    def __init__(self, dburi, dbname, level='AUTOCOMMIT'):
        self.dburi = dburi
        self.dbname = dbname
        self.engine = sqlalchemy.create_engine(
            self.dburi + self.dbname,
            isolation_level=level
        )

    @abc.abstractmethod
    def get_engine(self):
        pass
