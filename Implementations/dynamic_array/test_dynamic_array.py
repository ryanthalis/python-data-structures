import unittest

from dynamic_array import ArrayList


class ArrayListTests(unittest.TestCase):
    def test_extend(self) -> None:
        values = ArrayList([1, 2])
        values.extend((3, 4))
        self.assertEqual(list(values), [1, 2, 3, 4])

    def test_index_returns_first_match(self) -> None:
        values = ArrayList([10, 20, 10])
        self.assertEqual(values.index(10), 0)
        with self.assertRaises(ValueError):
            values.index(99)

    def test_pop(self) -> None:
        values = ArrayList([1, 2, 3])
        self.assertEqual(values.pop(), 3)
        self.assertEqual(values.pop(0), 1)
        self.assertEqual(list(values), [2])

    def test_pop_supports_negative_indices(self) -> None:
        values = ArrayList([10, 20, 30])
        self.assertEqual(values.pop(-2), 20)
        self.assertEqual(list(values), [10, 30])

    def test_pop_rejects_empty_or_invalid_index(self) -> None:
        with self.assertRaises(IndexError):
            ArrayList().pop()
        with self.assertRaises(IndexError):
            ArrayList([1]).pop(1)

    def test_reverse_iteration(self) -> None:
        self.assertEqual(list(reversed(ArrayList([1, 2, 3]))), [3, 2, 1])
        self.assertEqual(list(reversed(ArrayList())), [])


if __name__ == "__main__":
    unittest.main()
