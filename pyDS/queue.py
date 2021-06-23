class Queue(object):
    """docstring for Queue."""

    def __init__(self):
        super(Queue, self).__init__()
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def main():
    q = Queue()
    print(q.is_empty())
    q.enqueue("dog")
    q.enqueue(4)
    q = Queue()
    print(q.is_empty())
    q.enqueue(4)
    q.enqueue("dog")
    q.enqueue(True)
    print(q.size())
    print(q.is_empty())
    q.enqueue(8.4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())

if __name__ == '__main__':
    main()
