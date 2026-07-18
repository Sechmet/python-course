import unittest


class TestDivisibleByFour(unittest.TestCase):

    def setUp(self):
        self.result = [num for num in range(30, 81) if num % 4 == 0]

    def test_result_is_list(self):
        self.assertIsInstance(self.result, list)

    def test_all_numbers_divisible_by_4(self):
        for num in self.result:
            self.assertEqual(num % 4, 0)

    def test_all_numbers_in_range(self):
        for num in self.result:
            self.assertGreaterEqual(num, 30)
            self.assertLessEqual(num, 80)

    def test_first_number_is_32(self):
        self.assertEqual(self.result[0], 32)

    def test_last_number_is_80(self):
        self.assertEqual(self.result[-1], 80)

    def test_correct_count_of_numbers(self):
        self.assertEqual(len(self.result), 13)

    def test_correct_values(self):
        expected = [32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80]
        self.assertEqual(self.result, expected)


class TestFirst8OddNumbers(unittest.TestCase):

    def setUp(self):
        result = []
        num = 15
        while len(result) < 8:
            if num % 2 != 0:
                result.append(num)
            num += 1
        self.result = result

    def test_result_is_list(self):
        self.assertIsInstance(self.result, list)

    def test_exactly_8_numbers(self):
        self.assertEqual(len(self.result), 8)

    def test_all_numbers_are_odd(self):
        for num in self.result:
            self.assertNotEqual(num % 2, 0)

    def test_starts_at_15(self):
        self.assertEqual(self.result[0], 15)

    def test_correct_values(self):
        expected = [15, 17, 19, 21, 23, 25, 27, 29]
        self.assertEqual(self.result, expected)


class TestWeirdInput(unittest.TestCase):

    def test_empty_range_returns_no_divisible_numbers(self):
        result = [num for num in range(0, 0) if num % 4 == 0]
        self.assertEqual(result, [])

    def test_negative_numbers_divisible_by_4(self):
        result = [num for num in range(-20, -1) if num % 4 == 0]
        self.assertEqual(result, [-20, -16, -12, -8, -4])

    def test_range_with_no_divisible_by_4(self):
        result = [num for num in range(33, 36) if num % 4 == 0]
        self.assertEqual(result, [])

    def test_single_number_range_divisible_by_4(self):
        result = [num for num in range(32, 33) if num % 4 == 0]
        self.assertEqual(result, [32])

    def test_single_number_range_not_divisible_by_4(self):
        result = [num for num in range(33, 34) if num % 4 == 0]
        self.assertEqual(result, [])

    def test_odd_numbers_starting_from_zero(self):
        result = []
        num = 0
        while len(result) < 8:
            if num % 2 != 0:
                result.append(num)
            num += 1
        self.assertEqual(result[0], 1)
        self.assertEqual(len(result), 8)

    def test_odd_numbers_starting_from_negative(self):
        result = []
        num = -10
        while len(result) < 8:
            if num % 2 != 0:
                result.append(num)
            num += 1
        self.assertEqual(result, [-9, -7, -5, -3, -1, 1, 3, 5])

    def test_zero_odd_numbers_requested(self):
        result = []
        num = 15
        while len(result) < 0:
            if num % 2 != 0:
                result.append(num)
            num += 1
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
