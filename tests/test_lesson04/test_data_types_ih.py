# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116

import unittest

from lesson04.data_types_ih import first
from lesson04.data_types_ih import last


class TestDataTypesIh(unittest.TestCase):

    def test_first_is_str(self):

        sut = first
        print(sut)
        self.assertIsInstance(sut, str)

    def test_last_is_not_str(self):

        sut = last
        print(sut)
        self.assertNotIsInstance(sut, str)

    def test_last_is_float(self):

        sut = last
        print(sut)
        self.assertIsInstance(sut, float)


if __name__ == "__main__":
    unittest.main()
