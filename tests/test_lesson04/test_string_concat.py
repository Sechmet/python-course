# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116

import unittest

# ── string_concat ────────────────────────────────────────────────────────────
NUMBER: int = 1980
FLOAT_NUMBER: float = 42.0
STRING: str = "abcde"


class TestBasicConcat(unittest.TestCase):
    """Tests for basic string concatenation."""

    def test_concat_str_and_number(self):
        result = "1980" + str(NUMBER)
        self.assertEqual(result, "19801980")

    def test_concat_result_is_str(self):
        result = "1980" + str(NUMBER)
        self.assertIsInstance(result, str)

    def test_concat_fails_without_str_conversion(self):
        with self.assertRaises(TypeError):
            result = "1980" + NUMBER  # noqa: F841

    def test_concat_empty_string(self):
        result = "" + str(NUMBER)
        self.assertEqual(result, "1980")


class TestZeroPadding(unittest.TestCase):
    """Tests for zero-padding with f-strings."""

    def test_zero_padding_8_chars(self):
        result = f"{STRING} {NUMBER:08}"
        self.assertEqual(result, "abcde 00001980")

    def test_zero_padding_8_total_length(self):
        result = f"{NUMBER:08}"
        self.assertEqual(len(result), 8)

    def test_zero_padding_2_no_effect_when_number_longer(self):
        # width 2 is less than the number length, so no padding applied
        result = f"{STRING} {NUMBER:02}"
        self.assertEqual(result, "abcde 1980")

    def test_zero_padding_wider_than_needed(self):
        result = f"{NUMBER:012}"
        self.assertEqual(result, "000000001980")
        self.assertEqual(len(result), 12)

    def test_zero_padding_small_number(self):
        result = f"{5:08}"
        self.assertEqual(result, "00000005")


class TestFloatFormatting(unittest.TestCase):
    """Tests for float formatting with f-strings."""

    def test_float_format_8_width_4_decimals(self):
        result = f"{STRING} {FLOAT_NUMBER:08.4f}"
        self.assertEqual(result, "abcde 042.0000")

    def test_float_format_10_width_4_decimals(self):
        result = f"{STRING} {FLOAT_NUMBER:010.4f}"
        self.assertEqual(result, "abcde 00042.0000")

    def test_float_format_total_width(self):
        result = f"{FLOAT_NUMBER:010.4f}"
        self.assertEqual(len(result), 10)

    def test_float_format_3_decimals(self):
        result = f"{FLOAT_NUMBER:.3f}"
        self.assertEqual(result, "42.000")

    def test_float_format_zero_decimals(self):
        result = f"{FLOAT_NUMBER:.0f}"
        self.assertEqual(result, "42")


class TestPercentFormatting(unittest.TestCase):
    """Tests for % string formatting."""

    def test_percent_format_str_and_int(self):
        result = "%s %s" % (STRING, NUMBER)
        self.assertEqual(result, "abcde 1980")

    def test_percent_format_result_is_str(self):
        result = "%s %s" % (STRING, NUMBER)
        self.assertIsInstance(result, str)

    def test_percent_format_single_value(self):
        result = "%s" % STRING
        self.assertEqual(result, "abcde")

    def test_percent_format_does_not_use_curly_braces(self):
        result = "%s %s" % (STRING, NUMBER)
        self.assertNotIn("{", result)
        self.assertNotIn("}", result)


if __name__ == "__main__":
    unittest.main()
