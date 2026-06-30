# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        node = head
        n = 0
        
        while node and n < k:
            node = node.next
            n += 1
        
        if n < k:
            return head
        
        prev, cur = None, head
        for _ in range(k):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        head.next = self.reverseKGroup(cur, k)
        return prev
            