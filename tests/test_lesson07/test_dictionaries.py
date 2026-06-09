import unittest


class TestDictionaries(unittest.TestCase):

    def setUp(self):
        self.band = {
            "vocals": "Plant",
            "guitar": "Page"
        }

    def test_dict_length(self):
        self.assertEqual(len(self.band), 2)

    def test_access_by_key(self):
        self.assertEqual(self.band["vocals"], "Plant")

    def test_access_by_get(self):
        self.assertEqual(self.band.get("guitar"), "Page")

    def test_key_exists(self):
        self.assertIn("guitar", self.band)

    def test_key_not_exists(self):
        self.assertNotIn("triangle", self.band)

    def test_update_value(self):
        self.band["vocals"] = "Coverdale"
        self.assertEqual(self.band["vocals"], "Coverdale")

    def test_add_key(self):
        self.band.update({"bass": "JPJ"})
        self.assertIn("bass", self.band)

    def test_pop(self):
        self.band.update({"bass": "JPJ"})
        self.band.pop("bass")
        self.assertNotIn("bass", self.band)

    def test_copy_is_independent(self):
        band2 = self.band.copy()
        band2["drums"] = "Dave"
        self.assertNotIn("drums", self.band)

    def test_nested_dict(self):
        member1 = {"name": "Plant", "instrument": "vocals"}
        member2 = {"name": "Page", "instrument": "guitar"}
        band = {"member1": member1, "member2": member2}
        self.assertEqual(band["member1"]["name"], "Plant")

    def test_set_no_duplicates(self):
        nums = {1, 2, 2, 3}
        self.assertEqual(len(nums), 3)

    def test_set_union(self):
        one = {1, 2, 3}
        two = {5, 6, 7}
        self.assertEqual(one.union(two), {1, 2, 3, 5, 6, 7})

    def test_set_intersection(self):
        one = {1, 2, 3}
        two = {2, 3, 4}
        one.intersection_update(two)
        self.assertEqual(one, {2, 3})

    def test_set_symmetric_difference(self):
        one = {1, 2, 3}
        two = {2, 3, 4}
        one.symmetric_difference_update(two)
        self.assertEqual(one, {1, 4})


if __name__ == "__main__":
    unittest.main()