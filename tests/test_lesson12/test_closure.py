import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'lesson12'))
from closure import parent_function


class TestClosure(unittest.TestCase):

    def test_closure_returns_callable(self):
        play = parent_function("Tommy", 3)
        self.assertTrue(callable(play))

    def test_closure_decrements_coins(self):
        import io
        from contextlib import redirect_stdout
        play = parent_function("Tommy", 3)
        f = io.StringIO()
        with redirect_stdout(f):
            play()
        output = f.getvalue()
        self.assertIn("Tommy", output)
        self.assertIn("2", output)

    def test_closure_out_of_coins(self):
        import io
        from contextlib import redirect_stdout
        play = parent_function("Tommy", 1)
        f = io.StringIO()
        with redirect_stdout(f):
            play()
        output = f.getvalue()
        self.assertIn("out of coins", output)

    def test_two_closures_are_independent(self):
        tommy = parent_function("Tommy", 3)
        jenny = parent_function("Jenny", 5)
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            tommy()
        tommy_output = f.getvalue()
        f = io.StringIO()
        with redirect_stdout(f):
            jenny()
        jenny_output = f.getvalue()
        self.assertIn("Tommy", tommy_output)
        self.assertIn("Jenny", jenny_output)
        self.assertIn("2", tommy_output)
        self.assertIn("4", jenny_output)


if __name__ == "__main__":
    unittest.main()