import unittest
from data_structures import queue


class TestQueue(unittest.TestCase):
    def test_setup(self):
        q = queue.Queue()
        self.assertEqual(q.queue, [])

    def test_enqueue(self):
        q = queue.Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)

    def test_dequeue(self):
        q = queue.Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)


if __name__ == "__main__":
    unittest.main()
