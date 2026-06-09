import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'lesson09'))
from functions import sum, multiple_items, mult_named_items


class TestFunctions(unittest.TestCase):

    def test_sum_two_ints(self):
        self.assertEqual(sum(7, 2), 9)

    def test_sum_defaults_to_zero(self):
        self.assertEqual(sum(), 0)

    def test_sum_returns_zero_if_not_int(self):
        self.assertEqual(sum("a", 2), 0)

    def test_sum_returns_zero_if_both_not_int(self):
        self.assertEqual(sum("a", "b"), 0)

    def test_multiple_items_returns_tuple(self):
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            multiple_items("Dave", "John", "Sara")
        output = f.getvalue()
        self.assertIn("Dave", output)
        self.assertIn("John", output)
        self.assertIn("Sara", output)

    def test_mult_named_items_returns_dict(self):
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            mult_named_items(first="Dave", last="Gray")
        output = f.getvalue()
        self.assertIn("Dave", output)
        self.assertIn("Gray", output)


if __name__ == "__main__":
    unittest.main()