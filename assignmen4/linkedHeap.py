from chideraIbeh.assignmen4.binaryNode import BinaryNode


class LinkedHeap:
    def __init__(self):
        self.root = None
        self.last_node = None
        self.size = 0

    def insert(self, key, value):
        new_node = BinaryNode(key, value)
        if not self.root:
            self.root = new_node
            self.last_node = new_node
        else:
            self._insert_bubble_up(new_node)
        self.last_node = new_node
        self.size += 1

    def _insert_bubble_up(self, node):
        if not self.root:
            self.root = node
            return

        # Convert the size to binary and use it as a path to the insertion point
        path_to_insert = bin(self.size + 1)[3:]  # Skip the '0b1' part
        current = self.root

        # Navigate to the parent of the new node
        for direction in path_to_insert[:-1]:
            if direction == '0':
                if not current.left:
                    current.left = node
                    node.parent = current
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = node
                    node.parent = current
                    break
                current = current.right

        # Attach the new node at the correct spot
        if path_to_insert[-1] == '0':
            current.left = node
        else:
            current.right = node
        node.parent = current

        # Bubble up
        self._bubble_up(node)

    def _bubble_up(self, node):
        while node.parent and node.parent.key > node.key:
            node.key, node.parent.key = node.parent.key, node.key
            node.value, node.parent.value = node.parent.value, node.value
            node = node.parent

    def delete(self):
        if not self.root:
            return None
        min_node = self.root
        if self.last_node == self.root:
            self.root = None
            self.last_node = None
        else:
            self._delete_bubble_down()
        self.size -= 1
        return min_node.key, min_node.value

    def _delete_bubble_down(self):
        # If there's only one node in the heap
        if self.root == self.last_node:
            self.root = None
            self.last_node = None
            return

        # Swap the last node with the root
        self.root.key, self.last_node.key = self.last_node.key, self.root.key
        self.root.value, self.last_node.value = self.last_node.value, self.root.value

        # Store the last node's key and value to return later
        last_node_key, last_node_value = self.last_node.key, self.last_node.value

        # Find the parent of the last node
        parent_of_last = self._find_parent(self.root, self.last_node)

        # Detach the last node
        if parent_of_last.left == self.last_node:
            parent_of_last.left = None
        else:
            parent_of_last.right = None

        # Bubble down from the root
        self._bubble_down(self.root)

        # Update the last_node pointer
        self.last_node = self._get_new_last_node(self.root)

        return last_node_key, last_node_value

    def _find_parent(self, current, target):
        # Base case
        if not current:
            return None

        # If either left or right is the target, return this node (parent)
        if current.left == target or current.right == target:
            return current

        # Recursive case: search in left and right subtrees
        parent = self._find_parent(current.left, target)
        if parent:
            return parent
        return self._find_parent(current.right, target)

    def _get_new_last_node(self, root):
        if not root:
            return None
        queue = [root]
        last_node = None
        while queue:
            current = queue.pop(0)
            last_node = current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return last_node

    def _bubble_down(self, node):
        while node:
            left = node.left
            right = node.right
            smallest = node

            if left and left.key < smallest.key:
                smallest = left
            if right and right.key < smallest.key:
                smallest = right

            if smallest != node:
                # Swap values and keys with the smallest child
                node.key, smallest.key = smallest.key, node.key
                node.value, smallest.value = smallest.value, node.value
                node = smallest  # Continue bubbling down
            else:
                break

    def peek(self):
        return (self.root.key, self.root.value) if self.root else None
