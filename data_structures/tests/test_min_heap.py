import unittest

from data_structures.minheap import MinHeap


class TestHeap(unittest.TestCase):
    def test_setUp(self):
        h = MinHeap()
        self.assertEqual(h.heap, [])

    def test_insert(self):
        h = MinHeap()
        h.insert(1)
        h.insert(2)
        h.insert(3)
        self.assertEqual(h.heap, [1, 2, 3])

    def test_delete(self):
        h = MinHeap()
        h.insert(1)
        h.insert(2)
        h.insert(3)
        self.assertEqual(h.delete(), 1)
        self.assertEqual(h.heap, [2, 3])
