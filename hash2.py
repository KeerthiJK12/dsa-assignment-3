class SeparateChainingHashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def find(self, key):
        index = self._hash(key)
        for k, _ in self.buckets[index]:
            if k == key:
                return True
        return False

    def _resize(self, new_capacity):
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [[] for _ in range(new_capacity)]
        self.size = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self.insert(key, value)    

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)
                return
        self.buckets[index].append((key, value))
        self.size += 1
        if self.size > self.capacity * 0.75:
            self._resize(2 * self.capacity)

    def remove(self, key):
        index = self._hash(key)
        for i, (k, _) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]
                self.size -= 1
                if self.size < self.capacity * 0.25:
                    self._resize(self.capacity // 2)
                return   

sc_hashmap = SeparateChainingHashMap()
sc_hashmap.insert("key1", "value1")
sc_hashmap.insert("key2", "value2")
print(sc_hashmap.find("key1"))  
print(sc_hashmap.find("key3"))  
sc_hashmap.remove("key1")
print(sc_hashmap.find("key1"))  
