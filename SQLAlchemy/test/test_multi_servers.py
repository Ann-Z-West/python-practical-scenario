import unittest
from SQLAlchemy.database import session_maker, Student
from SQLAlchemy.test import count_student_server_in_container

""" Quick test - different Postgre servers
Before running this test case, please get prepared following instruction of test/README.md 
"""


class TestMultiDbServersBinding(unittest.TestCase):

    def test_count_student_in_master_server(self):
        """
        count students from local Postgre server's database test
        """
        row_count = 0
        with session_maker() as s:
            for st in s.query(Student):
                row_count += 1
        self.assertEqual(row_count, 1)

    def test_count_student_in_media_server(self):
        """
        count students from docker container Postgre server's database test
        """
        self.assertEqual(count_student_server_in_container(), 3)
