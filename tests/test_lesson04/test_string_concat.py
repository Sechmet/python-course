# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116

import unittest

# ── string_concat ────────────────────────────────────────────────────────────
NUMBER: int = 1980
FLOAT_NUMBER: float = 42.0
STRING: str = "abcde"


class TestStringConcat(unittest.TestCase):

    def test_basic_concat(self):
        result = "1980" + str(NUMBER)
        self.assertEqual(result, "19801980")

    def test_fstring_zero_padding_8(self):
        result = f"{STRING} {NUMBER:08}"
        self.assertEqual(result, "abcde 00001980")

    def test_fstring_zero_padding_2_no_effect(self):
        # width 2 is less than the number length, so no padding applied
        result = f"{STRING} {NUMBER:02}"
        self.assertEqual(result, "abcde 1980")

    def test_fstring_float_formatting8(self):
        result = f"{STRING} {FLOAT_NUMBER:08.4f}"
        print(result)
        self.assertEqual(result, "abcde 042.0000")

    def test_fstring_float_formatting10(self):
        result = f"{STRING} {FLOAT_NUMBER:010.4f}"
        print(result)
        self.assertEqual(result, "abcde 00042.0000")

    def test_percent_formatting(self):
        result = "%s %s" % (STRING, NUMBER)
        print(result)
        self.assertEqual(result, "abcde 1980")


if __name__ == "__main__":
    unittest.main()
