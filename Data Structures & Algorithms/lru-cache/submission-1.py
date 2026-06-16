class Node:
    def __init__(self, key=None, val=None, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cnt = 0
        self.hashMap = {}
        self.head, self.tail = Node(), Node()
        self.head.prev = self.tail
        self.tail.nxt = self.head
    
    def detach(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

        node.prev = None
        node.nxt = None

        self.cnt -= 1
    
    def add(self, node):
        node.nxt = self.head
        node.prev = self.head.prev

        self.head.prev.nxt = node
        self.head.prev = node

        self.cnt += 1
    
    def remove(self):
        if self.cnt == 0:
            return None

        node = self.tail.nxt
        self.detach(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1

        node = self.hashMap[key]

        self.detach(node)
        self.add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node = self.hashMap[key]
            node.val = value

            self.detach(node)
            self.add(node)
            return
        
        if self.cnt >= self.capacity:
            lru = self.remove()
            del self.hashMap[lru.key]
        
        node = Node(key, value)
        self.add(node)
        self.hashMap[key] = node

