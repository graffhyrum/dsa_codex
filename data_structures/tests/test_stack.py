import unittest
from data_structures import stack


class TestStack(unittest.TestCase):
    def test_setup(self):
        s = stack.Stack()
        self.assertEqual(s.stack, [])

    def test_push(self):
        s = stack.Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)

    def test_pop(self):
        s = stack.Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)


if __name__ == "__main__":
    unittest.main()
