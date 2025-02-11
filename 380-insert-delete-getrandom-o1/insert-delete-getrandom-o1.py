from collections import defaultdict
class RandomizedSet:

    def __init__(self):
        self.value_to_idx = defaultdict(int)        
        self.values = []
    def insert(self, val: int) -> bool:
        if val in self.value_to_idx.keys():
            return False
        new_idx = len(self.values)
        self.values.append(val)
        self.value_to_idx[val] = new_idx 
        return True

    def remove(self, val: int) -> bool:
        if val not in self.value_to_idx.keys():
            return False
        cur_val_idx = self.value_to_idx[val]
        last_val_idx = len(self.values) -1
        #swap it with the last value 
        self.values[cur_val_idx],self.values[last_val_idx] = self.values[last_val_idx],self.values[cur_val_idx]
        self.value_to_idx[self.values[cur_val_idx]] = cur_val_idx
        self.value_to_idx.pop(self.values[-1])
        self.values.pop()
        return True



    def getRandom(self) -> int:
        return self.values[random.randint(0,len(self.values) -1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()