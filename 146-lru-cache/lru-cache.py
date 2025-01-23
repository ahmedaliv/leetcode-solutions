class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def link(self, node1, node2):
        node1.next = node2
        node2.prev = node1

    def front(self):
        return self.head.next

    def back(self):
        return self.tail.prev

    def push_front(self, node):
        self.link(node, self.head.next)
        self.link(self.head, node)
        self.size += 1

    def erase(self, node):
        self.link(node.prev, node.next)
        self.size -= 1

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll = DoublyLinkedList()
        self.h_t = {}

    def get(self, key: int) -> int:
        if key not in self.h_t:
            return -1
        node = self.h_t[key]
        self.dll.erase(node)
        self.dll.push_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.h_t:
            node = self.h_t[key]
            self.dll.erase(node)
        elif self.dll.size == self.capacity:
            lru = self.dll.back()
            self.dll.erase(lru)
            del self.h_t[lru.key]
        new_node = Node(key, value)
        self.dll.push_front(new_node)
        self.h_t[key] = new_node
