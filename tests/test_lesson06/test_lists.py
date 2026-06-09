import unittest


class TestLists(unittest.TestCase):

    def setUp(self):
        self.users = ['Dave', 'John', 'Sara']
        self.data = ['Dave', 42, True]
        self.nums = [4, 42, 78, 1, 5]

    def test_empty_list_not_contains_dave(self):
        self.assertNotIn('Dave', [])

    def test_first_element(self):
        self.assertEqual(self.users[0], 'Dave')

    def test_negative_index(self):
        self.assertEqual(self.users[-2], 'John')

    def test_index_of(self):
        self.assertEqual(self.users.index('Sara'), 2)

    def test_slice(self):
        self.assertEqual(self.users[0:2], ['Dave', 'John'])

    def test_length(self):
        self.assertEqual(len(self.data), 3)

    def test_append(self):
        self.users.append('Elsa')
        self.assertIn('Elsa', self.users)

    def test_extend(self):
        self.users.extend(['Robert', 'Jimmy'])
        self.assertIn('Robert', self.users)
        self.assertIn('Jimmy', self.users)

    def test_insert(self):
        self.users.insert(0, 'Bob')
        self.assertEqual(self.users[0], 'Bob')

    def test_remove(self):
        self.users.remove('John')
        self.assertNotIn('John', self.users)

    def test_pop(self):
        last = self.users.pop()
        self.assertEqual(last, 'Sara')

    def test_sort(self):
        self.users.sort()
        self.assertEqual(self.users, ['Dave', 'John', 'Sara'])

    def test_reverse(self):
        self.nums.reverse()
        self.assertEqual(self.nums[0], 5)

    def test_copy(self):
        copy = self.nums.copy()
        copy.append(99)
        self.assertNotIn(99, self.nums)

    def test_tuple_immutable(self):
        mytuple = ('Dave', 42, True)
        with self.assertRaises(TypeError):
            mytuple[0] = 'John'

    def test_tuple_count(self):
        anothertuple = (1, 4, 2, 8, 2, 2)
        self.assertEqual(anothertuple.count(2), 3)

    def test_tuple_unpack(self):
        anothertuple = (1, 4, 2, 8, 2, 2)
        (one, *two, hey) = anothertuple
        self.assertEqual(one, 1)
        self.assertEqual(hey, 2)
        self.assertEqual(two, [4, 2, 8, 2])


if __name__ == "__main__":
    unittest.main()