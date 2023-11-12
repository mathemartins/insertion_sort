from chideraIbeh.assignmen4.linkedHeap import LinkedHeap


class PriorityQueue:
    def __init__(self):
        self.heap = LinkedHeap()

    def add(self, key, value):
        self.heap.insert(key, value)

    def remove(self):
        return self.heap.delete()

    def min(self):
        return self.heap.peek()

    def is_empty(self):
        return self.size() == 0

    def __len__(self):
        return self.heap.size
