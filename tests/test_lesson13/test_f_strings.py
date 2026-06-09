import unittest


class TestFStrings(unittest.TestCase):

    def setUp(self):
        self.person = "Dave"
        self.coins = 3

    def test_concatenation(self):
        result = "\n" + self.person + " has " + str(self.coins) + " coins left."
        self.assertEqual(result, "\nDave has 3 coins left.")

    def test_percent_formatting(self):
        message = "\n%s has %s coins left." % (self.person, self.coins)
        self.assertEqual(message, "\nDave has 3 coins left.")

    def test_str_format(self):
        message = "\n{} has {} coins left.".format(self.person, self.coins)
        self.assertEqual(message, "\nDave has 3 coins left.")

    def test_str_format_indexed(self):
        message = "\n{1} has {0} coins left.".format(self.coins, self.person)
        self.assertEqual(message, "\nDave has 3 coins left.")

    def test_str_format_named(self):
        message = "\n{person} has {coins} coins left.".format(
            coins=self.coins, person=self.person
        )
        self.assertEqual(message, "\nDave has 3 coins left.")

    def test_str_format_dict(self):
        player = {'person': 'Dave', 'coins': 3}
        message = "\n{person} has {coins} coins left.".format(**player)
        self.assertEqual(message, "\nDave has 3 coins left.")

    def test_fstring(self):
        message = f"\n{self.person} has {self.coins} coins left."
        self.assertEqual(message, "\nDave has 3 coins left.")

    def test_fstring_expression(self):
        message = f"\n{self.person} has {2 * 5} coins left."
        self.assertEqual(message, "\nDave has 10 coins left.")

    def test_fstring_method_call(self):
        message = f"\n{self.person.lower()} has {2 * 5} coins left."
        self.assertEqual(message, "\ndave has 10 coins left.")

    def test_fstring_float_format(self):
        num = 10
        result = f"2.25 times {num} is {2.25 * num:.2f}"
        self.assertEqual(result, "2.25 times 10 is 22.50")

    def test_fstring_percent_format(self):
        result = f"{1 / 4.52:.2%}"
        self.assertEqual(result, "22.12%")


if __name__ == "__main__":
    unittest.main()