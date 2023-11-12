To complete this assignment, you'll need to create two main data structures in Python: a `LinkedHeap` and a `PriorityQueue`. The `LinkedHeap` will be based on a linked tree structure using nodes and pointers, and the `PriorityQueue` will use the `LinkedHeap` as its underlying structure. Here's a general guideline on how to approach this:

### 1. BinaryNode Class
You need to use the provided `BinaryNode` class (or create an equivalent one if using another language). This class should represent a node in your binary heap, typically containing a key, a value, and pointers to left and right children.

### 2. LinkedHeap Class
This class will implement a min-heap using a linked tree structure. You need to define the following methods:

- `insert(key, value)`: Inserts a new node with the given key and value into the heap.
- `delete()`: Removes and returns the node with the minimum key.
- `peek()`: Returns the node with the minimum key without removing it from the heap.
- Helper methods as required for maintaining the heap property.

Remember, the heap property must be maintained at all times: the key of each node is greater than or equal to the key of its parent.

### 3. PriorityQueue Class
This class will use your `LinkedHeap` as its backing structure. Implement the following methods:

- `add(key, value)`: Adds a new (key, value) pair to the queue.
- `remove()`: Removes and returns the (key, value) pair with the minimum key.
- `min()`: Returns the (key, value) pair with the minimum key without removing it.
- `is_empty()`: Returns `True` if the queue is empty, `False` otherwise.
- `__len__()`: Returns the number of items in the queue.

### 4. Testing
To test your implementation, enqueue the items 11, 7, 8, 6, 5, 9, 4 and then dequeue three items. The dequeued items should be 4, 5, and 6, which are the items with the lowest keys.
