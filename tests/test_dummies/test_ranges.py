# Copyright 2026 Irene Hofstetter
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
import sys

sys.path.insert(0, ".")
from dummies.ranges import divisible_in_range, first_odd_numbers


class TestDivisibleByFour(unittest.TestCase):

    def setUp(self):
        self.result = divisible_in_range(30, 80, 4)

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
        self.result = first_odd_numbers(15, 8)

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


class TestDivisibleInRangeValidation(unittest.TestCase):

    def test_start_not_int_raises(self):
        with self.assertRaises(AssertionError):
            divisible_in_range(1.5, 80, 4)

    def test_stop_not_int_raises(self):
        with self.assertRaises(AssertionError):
            divisible_in_range(30, "80", 4)

    def test_divisor_not_int_raises(self):
        with self.assertRaises(AssertionError):
            divisible_in_range(30, 80, 2.0)

    def test_divisor_zero_raises(self):
        with self.assertRaises(AssertionError):
            divisible_in_range(30, 80, 0)

    def test_start_greater_than_stop_raises(self):
        with self.assertRaises(AssertionError):
            divisible_in_range(80, 30, 4)


class TestFirstOddNumbersValidation(unittest.TestCase):

    def test_start_not_int_raises(self):
        with self.assertRaises(AssertionError):
            first_odd_numbers(1.5, 8)

    def test_count_not_int_raises(self):
        with self.assertRaises(AssertionError):
            first_odd_numbers(15, "8")

    def test_negative_count_raises(self):
        with self.assertRaises(AssertionError):
            first_odd_numbers(15, -1)


if __name__ == "__main__":
    unittest.main()
