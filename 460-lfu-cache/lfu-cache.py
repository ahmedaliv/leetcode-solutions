from collections import defaultdict, OrderedDict

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1  # Every new node starts with frequency 1

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.min_freq = 0  # Track the minimum frequency for eviction
        self.dict = {}  # Key -> Node
        self.freq_to_list = defaultdict(OrderedDict)  # Frequency -> OrderedDict of (key -> Node)

    def update(self, node):
        """Updates the frequency of a node and moves it to the new frequency list."""
        freq = node.freq

        del self.freq_to_list[freq][node.key]

        if not self.freq_to_list[freq]:
            del self.freq_to_list[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        node.freq += 1
        new_freq = node.freq

        self.freq_to_list[new_freq][node.key] = node

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        node = self.dict[key]
        self.update(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.dict:
            node = self.dict[key]
            node.val = value 
            self.update(node)  
        else:
            if len(self.dict) >= self.cap:
                lfu_key, _ = self.freq_to_list[self.min_freq].popitem(last=False)  
                del self.dict[lfu_key]

            new_node = Node(key, value)
            self.dict[key] = new_node
            self.freq_to_list[1][key] = new_node
            self.min_freq = 1  # Reset min_freq to 1 for new entry
