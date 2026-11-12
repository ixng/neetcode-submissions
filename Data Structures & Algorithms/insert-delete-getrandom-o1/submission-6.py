import random
class RandomizedSet:

    def __init__(self):
        self.values = [] # list of values
        self.positions = {} # val -> pos
    def insert(self, val: int) -> bool: 
        if val in self.positions:
            return False
        self.positions[val] = len(self.positions)
        self.values.append(val)
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False
        lastVal = self.values[-1] 
        valPos = self.positions[val]

        self.values[valPos] = lastVal
        self.positions[lastVal] = valPos

        self.values.pop()
        del self.positions[val]
        return True 
    def getRandom(self) -> int:
        idx = random.randint(0,len(self.values) - 1)
        return self.values[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()