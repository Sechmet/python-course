import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'lesson15'))
from hello_person import hello
import io
from contextlib import redirect_stdout


class TestHelloPerson(unittest.TestCase):

    def test_hello_english(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hello("Dave", "English")
        self.assertEqual(f.getvalue().strip(), "Hello Dave!")

    def test_hello_spanish(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hello("Dave", "Spanish")
        self.assertEqual(f.getvalue().strip(), "Hola Dave!")

    def test_hello_german(self):
        f = io.StringIO()
        with redirect_stdout(f):
            hello("Dave", "German")
        self.assertEqual(f.getvalue().strip(), "Hallo Dave!")

    def test_hello_unknown_language_raises(self):
        with self.assertRaises(KeyError):
            hello("Dave", "French")


if __name__ == "__main__":
    unittest.main()