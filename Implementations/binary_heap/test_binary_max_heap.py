import unittest

from binary_max_heap import BinaryMaxHeap


class BinaryMaxHeapTests(unittest.TestCase):
    def test_add_and_peek(self) -> None:
        heap = BinaryMaxHeap()
        for value in (4, 9, 2, 7):
            heap.add(value)
        self.assertEqual(heap.peek(), 9)
        self.assertEqual(len(heap), 4)

    def test_remove_returns_descending_values(self) -> None:
        heap = BinaryMaxHeap([4, 9, 2, 7, 9])
        self.assertEqual([heap.remove() for _ in range(5)], [9, 9, 7, 4, 2])

    def test_delete_max_alias(self) -> None:
        heap = BinaryMaxHeap([1, 3, 2])
        self.assertEqual(heap.delete_max(), 3)

    def test_single_value(self) -> None:
        heap = BinaryMaxHeap([10])
        self.assertEqual(heap.remove(), 10)
        self.assertEqual(len(heap), 0)

    def test_empty_heap_errors(self) -> None:
        heap = BinaryMaxHeap()
        with self.assertRaises(IndexError):
            heap.peek()
        with self.assertRaises(IndexError):
            heap.remove()


if __name__ == "__main__":
    unittest.main()
