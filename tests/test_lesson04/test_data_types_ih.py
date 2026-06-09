# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116

import unittest

from lesson04.data_types_ih import first
from lesson04.data_types_ih import last


class TestFirst(unittest.TestCase):
    """Tests for the 'first' variable."""

    def test_first_is_str(self):
        self.assertIsInstance(first, str)

    def test_first_is_not_int(self):
        self.assertNotIsInstance(first, int)

    def test_first_is_not_float(self):
        self.assertNotIsInstance(first, float)

    def test_first_is_not_none(self):
        self.assertIsNotNone(first)

    def test_first_is_not_empty(self):
        self.assertGreater(len(first), 0)

    def test_first_value(self):
        self.assertEqual(first, "Irene")

    def test_first_is_not_a_number_string(self):
        self.assertFalse(first.isnumeric())


class TestLast(unittest.TestCase):
    """Tests for the 'last' variable."""

    def test_last_is_float(self):
        self.assertIsInstance(last, float)

    def test_last_is_not_str(self):
        self.assertNotIsInstance(last, str)

    def test_last_is_not_int(self):
        self.assertNotIsInstance(last, int)

    def test_last_is_not_none(self):
        self.assertIsNotNone(last)

    def test_last_value(self):
        self.assertEqual(last, 4.8)

    def test_last_is_not_zero(self):
        self.assertNotEqual(last, 0.0)

    def test_last_is_positive(self):
        self.assertGreater(last, 0)


if __name__ == "__main__":
    unittest.main()
