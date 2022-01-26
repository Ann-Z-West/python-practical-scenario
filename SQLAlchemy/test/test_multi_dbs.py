import unittest
from SQLAlchemy.database import session_maker
from SQLAlchemy.database import Student
from SQLAlchemy.test import count_student_local_server

""" Quick test - same Postgre server, different database
Before running this test case, please get prepared following instruction of test/README.md 
"""


class TestMultiDbSameServer(unittest.TestCase):
    def test_update_student(self):
        with session_maker() as s:
            for st in s.query(Student).filter(Student.name == "John Snow"):
                st.status = 7
            s.flush()
        with session_maker() as s:
            for st in s.query(Student).filter(Student.name == "John Snow"):
                self.assertEqual(st.status, 7)

    def test_count_student_in_media_db(self):
        self.assertEqual(count_student_local_server(), 2)
