import unittest



class TestListAccess(unittest.TestCase):
    """Tests for accessing list elements."""

    def setUp(self):
        self.users = ['Dave', 'John', 'Sara']






    def test_first_element(self):
        self.assertEqual(self.users[0], 'Dave')

    def test_negative_index(self):
        self.assertEqual(self.users[-2], 'John')

    def test_index_of(self):
        self.assertEqual(self.users.index('Sara'), 2)

    def test_slice(self):
        self.assertEqual(self.users[0:2], ['Dave', 'John'])



    def test_empty_list_not_contains_dave(self):
        self.assertNotIn('Dave', [])

    def test_index_out_of_range_raises(self):
        with self.assertRaises(IndexError):
            _ = self.users[10]

    def test_index_of_nonexistent_raises(self):
        with self.assertRaises(ValueError):
            self.users.index('Nobody')

    def test_negative_index_out_of_range_raises(self):
        with self.assertRaises(IndexError):
            _ = self.users[-10]


class TestListMutation(unittest.TestCase):
    """Tests for mutating lists."""

    def setUp(self):
        self.users = ['Dave', 'John', 'Sara']
        self.nums = [4, 42, 78, 1, 5]

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

    def test_remove_nonexistent_raises(self):
        with self.assertRaises(ValueError):
            self.users.remove('Nobody')

    def test_pop(self):
        last = self.users.pop()
        self.assertEqual(last, 'Sara')

    def test_pop_empty_list_raises(self):
        with self.assertRaises(IndexError):
            [].pop()

    def test_sort(self):
        self.users.sort()
        self.assertEqual(self.users, ['Dave', 'John', 'Sara'])

    def test_sort_mixed_types_raises(self):
        mixed = [1, 'a', 2]
        with self.assertRaises(TypeError):
            mixed.sort()

    def test_reverse(self):
        self.nums.reverse()
        self.assertEqual(self.nums[0], 5)


    def test_copy_is_independent(self):
        copy = self.nums.copy()
        copy.append(99)
        self.assertNotIn(99, self.nums)

    def test_length(self):
        self.assertEqual(len(self.users), 3)

    def test_clear_empties_list(self):
        self.users.clear()
        self.assertEqual(len(self.users), 0)


class TestTuples(unittest.TestCase):
    """Tests for tuples."""

    def test_tuple_immutable(self):
        mytuple = ('Dave', 42, True)
        with self.assertRaises(TypeError):
            mytuple[0] = 'John'

    def test_tuple_count(self):
        anothertuple = (1, 4, 2, 8, 2, 2)
        self.assertEqual(anothertuple.count(2), 3)

    def test_tuple_count_nonexistent_returns_zero(self):
        anothertuple = (1, 4, 2, 8, 2, 2)
        self.assertEqual(anothertuple.count(99), 0)

    def test_tuple_unpack(self):
        anothertuple = (1, 4, 2, 8, 2, 2)
        (one, *two, hey) = anothertuple
        self.assertEqual(one, 1)
        self.assertEqual(hey, 2)
        self.assertEqual(two, [4, 2, 8, 2])

    def test_tuple_index_out_of_range_raises(self):
        mytuple = ('Dave', 42, True)
        with self.assertRaises(IndexError):
            _ = mytuple[10]


if __name__ == "__main__":
    unittest.main()