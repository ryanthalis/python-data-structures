import contextlib
import io
import unittest

from avl_tree import AVLTree


def build_tree(values):
    root = AVLTree(values[0])
    with contextlib.redirect_stdout(io.StringIO()):
        for value in values[1:]:
            root = root.insert(value)
    return root


class AVLTreeTests(unittest.TestCase):
    def test_insert_and_search(self):
        root = build_tree([30, 20, 40, 10, 5])
        self.assertEqual(list(root), [5, 10, 20, 30, 40])
        self.assertEqual(root.search(20).item, 20)
        self.assertIsNone(root.search(99))

    def test_left_right_rotation(self):
        root = build_tree([30, 10, 20])
        self.assertEqual(root.item, 20)
        self.assertEqual((root.left.item, root.right.item), (10, 30))

    def test_right_left_rotation(self):
        root = build_tree([10, 30, 20])
        self.assertEqual(root.item, 20)
        self.assertEqual((root.left.item, root.right.item), (10, 30))

    def test_delete_node_with_left_child(self):
        root = build_tree([10, 5, 15, 2])
        with contextlib.redirect_stdout(io.StringIO()):
            root = root.delete(5)
        self.assertEqual(list(root), [2, 10, 15])

    def test_delete_node_with_two_children(self):
        root = build_tree([10, 5, 20, 15, 30])
        with contextlib.redirect_stdout(io.StringIO()):
            root = root.delete(20)
        self.assertEqual(list(root), [5, 10, 15, 30])

    def test_delete_missing_value(self):
        root = build_tree([10, 5, 15])
        self.assertIs(root.delete(99), root)


if __name__ == "__main__":
    unittest.main()
