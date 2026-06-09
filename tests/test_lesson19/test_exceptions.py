import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'lesson19'))
from exceptions import JustNotCoolError


class TestExceptions(unittest.TestCase):

    def test_custom_exception_is_exception(self):
        self.assertTrue(issubclass(JustNotCoolError, Exception))

    def test_raise_custom_exception(self):
        with self.assertRaises(JustNotCoolError):
            raise JustNotCoolError("This just isn't cool, man.")

    def test_custom_exception_message(self):
        try:
            raise JustNotCoolError("This just isn't cool, man.")
        except JustNotCoolError as e:
            self.assertEqual(str(e), "This just isn't cool, man.")

    def test_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            x = 1 / 0

    def test_type_error(self):
        with self.assertRaises(TypeError):
            x = 2
            if not type(x) is str:
                raise TypeError("Only strings are allowed.")

    def test_try_except_else(self):
        result = None
        try:
            result = 10 / 2
        except ZeroDivisionError:
            result = 0
        else:
            result = "no error"
        self.assertEqual(result, "no error")

    def test_finally_always_runs(self):
        ran_finally = []
        try:
            raise ValueError("test")
        except ValueError:
            pass
        finally:
            ran_finally.append(True)
        self.assertTrue(ran_finally[0])


if __name__ == "__main__":
    unittest.main()