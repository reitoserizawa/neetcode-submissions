"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        originalCopy = {}

        cur = head
        while cur:
            node = Node(cur.val)
            originalCopy[cur] = node
            cur = cur.next
        
        cur = head
        while cur:
            node = originalCopy[cur]
            if cur.next:
                node.next = originalCopy[cur.next]
            if cur.random:
                node.random = originalCopy[cur.random]
            cur = cur.next
        
        return originalCopy[head] if head else None
