import unittest

from algorithms.sort import quicksort

class TestQuicksort(unittest.TestCase):
    def test_quicksort(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sorted_arr = quicksort.quicksort(arr)
        self.assertEqual(sorted_arr, [1, 1, 2, 3, 6, 8, 10])

    def test_quicksort_empty(self):
        arr = []
        sorted_arr = quicksort.quicksort(arr)
        self.assertEqual(sorted_arr, [])

    def test_quicksort_single(self):
        arr = [1]
        sorted_arr = quicksort.quicksort(arr)
        self.assertEqual(sorted_arr, [1])

    def test_quicksort_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorted_arr = quicksort.quicksort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_quicksort_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorted_arr = quicksort.quicksort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_quicksort_duplicates(self):
        arr = [1, 1, 1, 2, 1]
        sorted_arr = quicksort.quicksort(arr)
        self.assertEqual(sorted_arr, [1, 1, 1, 1, 2])

    def test_quicksort_negative(self):
        arr = [-1, -2, -3, -4, -5]
        sorted_arr = quicksort.quicksort(arr)
        self.assertEqual(sorted_arr, [-5, -4, -3, -2, -1])

    def test_quicksort_mixed(self):
        arr = [-1, 2, -3, 4, -5]
        sorted_arr = quicksort.quicksort(arr)
        self.assertEqual(sorted_arr, [-5, -3, -1, 2, 4])

    def test_quicksort_floats(self):
        arr = [7.7, 1.1, 2.2, 3.3, 4.4, 5.5]
        sorted_arr = quicksort.quicksort(arr)
        self.assertEqual(sorted_arr, [1.1, 2.2, 3.3, 4.4, 5.5, 7.7])