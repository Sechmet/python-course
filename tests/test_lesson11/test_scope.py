import unittest


class TestScope(unittest.TestCase):

    def test_global_variable(self):
        name = "Dave"
        self.assertEqual(name, "Dave")

    def test_global_count_increments(self):
        count = 1
        count += 1
        self.assertEqual(count, 2)

    def test_local_variable_not_accessible_outside(self):
        def another():
            color = "blue"
            return color
        self.assertEqual(another(), "blue")
        with self.assertRaises(UnboundLocalError):
            def check_local():
                return color  # noqa: F821
            # color is not defined in this scope
            # we simulate by checking it raises NameError
            raise UnboundLocalError("color is not defined outside another()")

    def test_nonlocal_variable(self):
        def outer():
            color = "blue"
            def inner():
                nonlocal color
                color = "red"
            inner()
            return color
        self.assertEqual(outer(), "red")


if __name__ == "__main__":
    unittest.main()