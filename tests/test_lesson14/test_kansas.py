import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'lesson14'))
import kansas


class TestKansas(unittest.TestCase):

    def test_capital(self):
        self.assertEqual(kansas.capital, "Topeka")

    def test_bird(self):
        self.assertEqual(kansas.bird, "Western Meadowlark")

    def test_flower(self):
        self.assertEqual(kansas.flower, "Sunflower")

    def test_song(self):
        self.assertEqual(kansas.song, "Home on the Range")

    def test_randomfunfact_prints_something(self):
        import io
        from contextlib import redirect_stdout
        f = io.StringIO()
        with redirect_stdout(f):
            kansas.randomfunfact()
        output = f.getvalue()
        self.assertTrue(len(output) > 0)

    def test_randomfunfact_is_one_of_known_facts(self):
        import io
        from contextlib import redirect_stdout
        known_facts = [
            "Kansas is considered flat",
            "Wichita is the largest city",
            "Kansas City is actually in Missouri",
            "Wizard of Oz"
        ]
        f = io.StringIO()
        with redirect_stdout(f):
            kansas.randomfunfact()
        output = f.getvalue()
        self.assertTrue(any(fact in output for fact in known_facts))


if __name__ == "__main__":
    unittest.main()