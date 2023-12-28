# A queue

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        val = self.queue[0]
        del self.queue[0]
        return val