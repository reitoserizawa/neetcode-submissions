class Node:
    def __init__(self, val=-1, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.nxt = nxt


class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.head, self.tail = Node(), Node()
        self.head.prev = self.tail
        self.tail.nxt = self.head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value)
        node.nxt = self.head
        node.prev = self.head.prev

        node.prev.nxt = node
        self.head.prev = node

        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        node = self.tail.nxt

        self.tail.nxt = node.nxt
        node.nxt.prev = self.tail


        self.size -= 1
        
        return True

        

    def Front(self) -> int:
        return self.tail.nxt.val 
        

    def Rear(self) -> int:
        return self.head.prev.val
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()