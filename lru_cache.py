class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
            self.size -= 1
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        self.size += 1
        if self.size > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
            self.size -= 1


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  
lru.put(3, 3)     
print(lru.get(2))  
lru.put(4, 4)     
print(lru.get(1))
print(lru.get(3))  

