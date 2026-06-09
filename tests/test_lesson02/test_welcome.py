import unittest


class TestWelcome(unittest.TestCase):

    def test_header_footer_value(self):
        line01 = "********************"
        self.assertEqual(line01, "********************")

    def test_header_footer_length(self):
        line01 = "********************"
        self.assertEqual(len(line01), 20)

    def test_body_value(self):
        line02 = "*                  *"
        self.assertEqual(line02, "*                  *")

    def test_body_length(self):
        line02 = "*                  *"
        self.assertEqual(len(line02), 20)

    def test_welcome_value(self):
        line03 = "*     WELCOME!     *"
        self.assertEqual(line03, "*     WELCOME!     *")

    def test_all_lines_same_length(self):
        line01 = "********************"
        line02 = "*                  *"
        line03 = "*     WELCOME!     *"
        self.assertEqual(len(line01), len(line02))
        self.assertEqual(len(line02), len(line03))


if __name__ == "__main__":
    unittest.main()