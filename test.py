import unittest
from asd import my_func


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(my_func(1,2), 3)