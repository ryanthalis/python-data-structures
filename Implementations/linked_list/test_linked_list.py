import unittest

from linked_list import LinkedList


class LinkedListTests(unittest.TestCase):
    def test_membership(self) -> None:
        self.assertIn(20, LinkedList([10, 20, 30]))
        self.assertNotIn(10, LinkedList())

    def test_equality(self) -> None:
        self.assertEqual(LinkedList([1, 2, 3]), LinkedList([1, 2, 3]))
        self.assertNotEqual(LinkedList([1, 2, 3]), LinkedList([1, 4, 3]))
        self.assertNotEqual(LinkedList([1, 2]), [1, 2])

    def test_delete(self) -> None:
        values = LinkedList([1, 2, 3])
        del values[1]
        self.assertEqual(list(values), [1, 3])
        with self.assertRaises(IndexError):
            del values[5]

    def test_remove_first_match(self) -> None:
        values = LinkedList([3, 1, 3, 4])
        values.remove(3)
        self.assertEqual(list(values), [1, 3, 4])

    def test_single_item_removal_preserves_list(self) -> None:
        values = LinkedList([10])
        values.remove(10)
        values.append(20)
        self.assertEqual(list(values), [20])

    def test_remove_rejects_missing_value(self) -> None:
        with self.assertRaises(ValueError):
            LinkedList().remove(10)


if __name__ == "__main__":
    unittest.main()
