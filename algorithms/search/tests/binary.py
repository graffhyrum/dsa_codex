import unittest

from algorithms.search import binary

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5]
        index = binary.binary_search(arr, 4)
        self.assertEqual(index, 3)

    def test_binary_search_empty(self):
        arr = []
        index = binary.binary_search(arr, 4)
        self.assertEqual(index, None)

    def test_binary_search_single(self):
        arr = [1]
        index = binary.binary_search(arr, 1)
        self.assertEqual(index, 0)

    def test_binary_search_not_found(self):
        arr = [1, 2, 3, 4, 5]
        index = binary.binary_search(arr, 6)
        self.assertEqual(index, None)

    def test_binary_search_negative(self):
        arr = [-5, -4, -3, -2, -1]
        index = binary.binary_search(arr, -3)
        self.assertEqual(index, 2)

    def test_binary_search_mixed(self):
        arr = [-5, -3, -1, 2, 4]
        index = binary.binary_search(arr, 2)
        self.assertEqual(index, 3)

    def test_binary_search_floats(self):
        arr = [1.1, 2.2, 3.3, 4.4, 5.5, 7.7]
        index = binary.binary_search(arr, 5.5)
        self.assertEqual(index, 4)

    def test_big_search(self):
        arr = [i for i in range(1000000)]
        index = binary.binary_search(arr, 999999)
        self.assertEqual(index, 999999)