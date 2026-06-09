import unittest

# ── meaning.py ─────────────────────────────────────────────────────────────
meaning = 42


class TestMeaningType(unittest.TestCase):
    """Tests for the type of meaning."""

    def test_meaning_is_int(self):
        self.assertIsInstance(meaning, int)

    def test_meaning_is_not_str(self):
        self.assertNotIsInstance(meaning, str)

    def test_meaning_is_not_float(self):
        self.assertNotIsInstance(meaning, float)

    def test_meaning_is_not_none(self):
        self.assertIsNotNone(meaning)


class TestMeaningValue(unittest.TestCase):
    """Tests for the value of meaning."""

    def test_meaning_equals_42(self):
        self.assertEqual(meaning, 42)

    def test_meaning_is_not_zero(self):
        self.assertNotEqual(meaning, 0)

    def test_meaning_is_not_negative(self):
        self.assertGreater(meaning, 0)

    def test_meaning_greater_than_10(self):
        self.assertGreater(meaning, 10)

    def test_meaning_less_than_100(self):
        self.assertLess(meaning, 100)


class TestTernaryOperator(unittest.TestCase):
    """Tests for the ternary operator logic."""

    def test_ternary_right_on_when_greater_than_10(self):
        value = 42
        result = "Right on!" if value > 10 else "Not today"
        self.assertEqual(result, "Right on!")

    def test_ternary_not_today_when_equal_to_10(self):
        value = 10
        result = "Right on!" if value > 10 else "Not today"
        self.assertEqual(result, "Not today")

    def test_ternary_not_today_when_less_than_10(self):
        value = 5
        result = "Right on!" if value > 10 else "Not today"
        self.assertEqual(result, "Not today")

    def test_ternary_not_today_when_zero(self):
        value = 0
        result = "Right on!" if value > 10 else "Not today"
        self.assertEqual(result, "Not today")

    def test_ternary_not_today_when_negative(self):
        value = -5
        result = "Right on!" if value > 10 else "Not today"
        self.assertEqual(result, "Not today")

    def test_ternary_right_on_with_meaning(self):
        result = "Right on!" if meaning > 10 else "Not today"
        self.assertEqual(result, "Right on!")


if __name__ == "__main__":
    unittest.main()
