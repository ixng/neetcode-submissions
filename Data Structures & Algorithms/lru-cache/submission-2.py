class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key , node 

        self.lru = Node(0,0)
        self.mru = Node(0,0)

        self.lru.next = self.mru
        self.mru.prev = self.lru

    def remove(self,node):
        left = node.prev
        right = node.next
        right.prev = left
        left.next = right



    def insert(self,node):
        actual_mru = self.mru.prev
        actual_mru.next = node
        node.prev = actual_mru
        node.next = self.mru
        self.mru.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]
        


        
