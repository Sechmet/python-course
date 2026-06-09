import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'lesson10'))
from recursion import add_one


class TestRecursion(unittest.TestCase):

    def test_add_one_from_zero(self):
        self.assertEqual(add_one(0), 10)

    def test_add_one_from_five(self):
        self.assertEqual(add_one(5), 10)

    def test_add_one_at_nine(self):
        self.assertEqual(add_one(9), 10)

    def test_add_one_above_nine(self):
        self.assertEqual(add_one(15), 16)


if __name__ == "__main__":
    unittest.main()