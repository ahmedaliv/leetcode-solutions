from collections import deque

class DLLNode:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class SortedDictDLL:
    def __init__(self):
        self.map = {}  # HashMap: {col: list of (row, val)}
        self.head = None
        self.tail = None

    def insert(self, col):
        if col in self.map:
            return
        
        node = DLLNode(col)
        self.map[col] = []  # Initialize column list
        
        if not self.head:  # First insertion
            self.head = self.tail = node
            return
        
        # Maintain sorted order in DLL
        curr = self.head
        while curr and curr.key < col:
            prev = curr
            curr = curr.next
        
        if curr == self.head:  # Insert at head
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif curr is None:  # Insert at tail
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:  # Insert in middle
            prev.next = node
            node.prev = prev
            node.next = curr
            curr.prev = node

    def get_sorted_keys(self):
        result = []
        curr = self.head
        while curr:
            result.append(curr.key)
            curr = curr.next
        return result


class Solution:

    def verticalTraversal(self,root):
        if not root:
            return []

        node_map = SortedDictDLL()
        queue = deque([(root, 0, 0)])

        while queue:
            node, row, col = queue.popleft()
            node_map.insert(col)
            node_map.map[col].append((row, node.val))
            
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        
        result = []
        for col in node_map.get_sorted_keys():
            result.append([val for row, val in sorted(node_map.map[col])])

        return result