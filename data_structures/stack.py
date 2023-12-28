# A stack

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        val = self.stack[-1]
        del self.stack[-1]
        return val
