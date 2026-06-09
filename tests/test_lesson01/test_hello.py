import unittest


class TestHello(unittest.TestCase):

    def test_greeting_is_str(self):
        greeting = 'Hello World!'
        self.assertIsInstance(greeting, str)

    def test_greeting_value(self):
        greeting = 'Hello World!'
        self.assertEqual(greeting, 'Hello World!')


if __name__ == "__main__":
    unittest.main()