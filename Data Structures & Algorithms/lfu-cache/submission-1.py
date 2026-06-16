class Node:
    def __init__(self, key=None, val=None, freq=1):
        self.key=key
        self.val=val
        self.freq = freq
        self.prev=None
        self.nxt=None

class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head, self.tail = Node(freq=0), Node(freq=0)
        self.head.prev = self.tail
        self.tail.nxt = self.head
    
    def add(self, node):
        prev = self.head.prev

        prev.nxt = node        
        node.prev = prev

        node.nxt = self.head
        self.head.prev = node

        self.size += 1

        return node
    
    def detach(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

        node.prev = None
        node.nxt = None

        self.size -= 1
    
    def remove(self):
        node = self.tail.nxt
        self.detach(self.tail.nxt)

        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # key: node
        self.hashMap = {}
        # freq: DL
        self.freqMap = defaultdict(DoublyLinkedList)
        self.minFreq = 0

    def get(self, key: int) -> int:
        if not key in self.hashMap:
            return -1
        
        node = self.hashMap[key]
        old_freq = node.freq
        self.freqMap[old_freq].detach(node)

        if self.freqMap[old_freq].size == 0:
            del self.freqMap[old_freq]
            if old_freq == self.minFreq:
                self.minFreq += 1

        node.freq += 1
        self.freqMap[node.freq].add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node = self.hashMap[key]
            node.val = value
            old_freq = node.freq
            self.freqMap[old_freq].detach(node)
            if self.freqMap[old_freq].size == 0:
                del self.freqMap[old_freq]
                if self.minFreq == old_freq:
                    self.minFreq += 1
            node.freq += 1
    
        else:
            if self.capacity == 0:
                removed = self.freqMap[self.minFreq].remove()
                del self.hashMap[removed.key]

                if self.freqMap[self.minFreq].size == 0:
                    del self.freqMap[self.minFreq]

            else:
                self.capacity -= 1

            node = Node(key, value)
            self.minFreq = 1

        self.freqMap[node.freq].add(node)
        self.hashMap[key] = node
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)