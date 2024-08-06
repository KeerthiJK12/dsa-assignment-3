class LinearProbingHashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * capacity
        self.values = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity



    def _probe(self, index):
        return (index + 1) % self.capacity


    def find(self, key):
        index = self._hash(key)
        for _ in range(self.capacity):
            if self.keys[index] == key:
                return True
            if self.keys[index] is None:
                return False
            index = self._probe(index)
        return False


    def insert(self, key, value):
        if self.size >= self.capacity // 2:
            self._resize(2 * self.capacity)
        index = self._hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return
            index = self._probe(index)
        self.keys[index] = key
        self.values[index] = value
        self.size += 1
 
    def _resize(self, new_capacity):
        old_keys = self.keys
        old_values = self.values
        self.capacity = new_capacity
        self.keys = [None] * new_capacity
        self.values = [None] * new_capacity
        self.size = 0
        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self.insert(old_keys[i], old_values[i])




    def remove(self, key):
        index = self._hash(key)
        for _ in range(self.capacity):
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.size -= 1
                index = self._probe(index)
                while self.keys[index] is not None:
                    key_to_rehash = self.keys[index]
                    value_to_rehash = self.values[index]
                    self.keys[index] = None
                    self.values[index] = None
                    self.size -= 1
                    self.insert(key_to_rehash, value_to_rehash)
                    index = self._probe(index)
                if self.size > 0 and self.size <= self.capacity // 8:
                    self._resize(self.capacity // 2)
                return
            index = self._probe(index)

lp_hashmap = LinearProbingHashMap()
lp_hashmap.insert("key1", "value1")
lp_hashmap.insert("key2", "value2")
print(lp_hashmap.find("key1")) 
print(lp_hashmap.find("key3"))  
lp_hashmap.remove("key1")
print(lp_hashmap.find("key1"))
