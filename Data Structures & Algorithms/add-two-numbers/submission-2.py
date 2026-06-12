# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        increment = 0

        while l1 or l2:
            n = (l1.val if l1 else 0) + (l2.val if l2 else 0) + increment
            m = n % 10
            node = ListNode(m)
            tail.next = node
            tail = node
            increment = n // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if increment:
            node = ListNode(increment)
            tail.next = node
            tail = node
        
        return dummy.next