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

"""Utility functions for working with ranges and odd numbers."""


def divisible_in_range(start: int, stop: int, divisor: int) -> list[int]:
    """Return all integers between start and stop (inclusive) divisible by divisor."""
    assert isinstance(start, int), "start must be an integer"
    assert isinstance(stop, int), "stop must be an integer"
    assert isinstance(divisor, int), "divisor must be an integer"
    assert divisor != 0, "divisor must not be zero"
    assert start <= stop, "start must be less than or equal to stop"
    return [num for num in range(start, stop + 1) if num % divisor == 0]


def first_odd_numbers(start: int, count: int) -> list[int]:
    """Return the first 'count' odd numbers starting from 'start'."""
    assert isinstance(start, int), "start must be an integer"
    assert isinstance(count, int), "count must be an integer"
    assert count >= 0, "count must be zero or greater"
    result: list[int] = []
    num = start
    while len(result) < count:
        if num % 2 != 0:
            result.append(num)
        num += 1
    return result


if __name__ == "__main__":
    print("Print all numbers between 30 and 80 that are divisible by 4")
    print("")
    print(divisible_in_range(30, 80, 4))
    print("")

    print("Print the first 8 odd numbers starting from 15")
    print("")
    odd_numbers = first_odd_numbers(15, 8)
    print(odd_numbers)
    print("")
