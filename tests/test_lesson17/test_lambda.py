import unittest
from functools import reduce


class TestLambda(unittest.TestCase):

    def test_squared(self):
        squared = lambda num: num * num
        self.assertEqual(squared(2), 4)
        self.assertEqual(squared(5), 25)

    def test_add_two(self):
        add_two = lambda num: num + 2
        self.assertEqual(add_two(12), 14)

    def test_sum_total(self):
        sum_total = lambda a, b: a + b
        self.assertEqual(sum_total(10, 8), 18)

    def test_func_builder(self):
        def funcBuilder(x):
            return lambda num: num + x
        add_ten = funcBuilder(10)
        add_twenty = funcBuilder(20)
        self.assertEqual(add_ten(7), 17)
        self.assertEqual(add_twenty(7), 27)

    def test_map(self):
        numbers = [3, 7, 12, 18, 20, 21]
        squared_nums = list(map(lambda num: num * num, numbers))
        self.assertEqual(squared_nums, [9, 49, 144, 324, 400, 441])

    def test_filter(self):
        numbers = [3, 7, 12, 18, 20, 21]
        odd_nums = list(filter(lambda num: num % 2 != 0, numbers))
        self.assertEqual(odd_nums, [3, 7, 21])

    def test_reduce(self):
        numbers = [1, 2, 3, 4, 5, 1]
        total = reduce(lambda acc, curr: acc + curr, numbers, 10)
        self.assertEqual(total, 26)

    def test_reduce_char_count(self):
        names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']
        char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
        self.assertEqual(char_count, 47)


if __name__ == "__main__":
    unittest.main()