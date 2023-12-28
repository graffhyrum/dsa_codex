import unittest
from data_structures import binary_tree


class TestBinaryTree(unittest.TestCase):
    def test_setup(self):
        root = binary_tree.Node(1)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left, None)
        self.assertEqual(root.right, None)

    def test_insert(self):
        root = binary_tree.Node(1)
        root.insert(2)
        root.insert(3)
        self.assertEqual(root.right.val, 2)
        self.assertEqual(root.right.right.val, 3)

    def test_insert_left(self):
        root = binary_tree.Node(1)
        root.insert(0)
        root.insert(-1)
        self.assertEqual(root.left.val, 0)
        self.assertEqual(root.left.left.val, -1)

    def test_insert_left_right(self):
        root = binary_tree.Node(1)
        root.insert(0)
        root.insert(2)
        self.assertEqual(root.left.val, 0)
        self.assertEqual(root.right.val, 2)

    def test_print_tree(self):
        root = binary_tree.Node(1)
        root.insert(2)
        root.insert(3)
        root.insert(4)
        root.insert(5)
        root.insert(6)
        root.insert(7)
        root.print_tree()


if __name__ == "__main__":
    unittest.main()
