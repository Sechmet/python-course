import unittest


class TestLoops(unittest.TestCase):

    def test_range_step(self):
        result = list(range(5, 101, 5))
        self.assertEqual(result[0], 5)
        self.assertEqual(result[-1], 100)
        self.assertEqual(len(result), 20)

    def test_for_loop_over_list(self):
        names = ["Dave", "Sara", "John"]
        result = []
        for x in names:
            result.append(x)
        self.assertEqual(result, ["Dave", "Sara", "John"])

    def test_nested_loop(self):
        names = ["Dave", "Sara"]
        actions = ["codes", "eats"]
        result = []
        for action in actions:
            for name in names:
                result.append(name + " " + action + ".")
        self.assertEqual(result[0], "Dave codes.")
        self.assertEqual(result[1], "Sara codes.")
        self.assertEqual(result[2], "Dave eats.")
        self.assertEqual(result[3], "Sara eats.")

    def test_while_loop(self):
        value = 1
        result = []
        while value <= 5:
            result.append(value)
            value += 1
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_break(self):
        names = ["Dave", "Sara", "John"]
        result = []
        for x in names:
            if x == "Sara":
                break
            result.append(x)
        self.assertEqual(result, ["Dave"])

    def test_continue(self):
        names = ["Dave", "Sara", "John"]
        result = []
        for x in names:
            if x == "Sara":
                continue
            result.append(x)
        self.assertEqual(result, ["Dave", "John"])


if __name__ == "__main__":
    unittest.main()