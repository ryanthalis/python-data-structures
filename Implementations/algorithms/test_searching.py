import unittest

from searching import binary_search, sequential_search


class SequentialSearchTests(unittest.TestCase):
    def test_finds_first_match(self):
        self.assertEqual(sequential_search([4, 7, 7, 9], 7), 1)

    def test_missing_or_empty(self):
        self.assertEqual(sequential_search([1, 2, 3], 8), -1)
        self.assertEqual(sequential_search([], 8), -1)


class BinarySearchTests(unittest.TestCase):
    def test_finds_values(self):
        values = [2, 4, 6, 8, 10]
        self.assertEqual(binary_search(values, 2), 0)
        self.assertEqual(binary_search(values, 6), 2)
        self.assertEqual(binary_search(values, 10), 4)

    def test_missing_or_empty(self):
        self.assertEqual(binary_search([2, 4, 6], 5), -1)
        self.assertEqual(binary_search([], 5), -1)


if __name__ == "__main__":
    unittest.main()
