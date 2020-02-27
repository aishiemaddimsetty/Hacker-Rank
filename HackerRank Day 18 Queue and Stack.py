class Palindrome():
    def __init__(self, stack, queue, size):
        self.stack = []
        self.queue = []

    def Push(self, data):
        self.stack.append(data)

    def enqeue(self, data):
        self.queue.append(data)

    def pop(self):
        itemPopped = self.stack.pop()

    def dequeue(self):
        itemDequeued = self.queue.pop(0)


string = Palindrome()

