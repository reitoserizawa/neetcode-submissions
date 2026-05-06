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
        originalToCopy = {}
        cur = head

        while cur:
            node = Node(cur.val)
            originalToCopy[cur] = node
            cur = cur.next
        
        cur = head
        while cur:
            node = originalToCopy[cur]
            if cur.next:
                node.next = originalToCopy[cur.next]
            if cur.random:
                node.random = originalToCopy[cur.random]
            cur = cur.next

        return originalToCopy[head] if head else None