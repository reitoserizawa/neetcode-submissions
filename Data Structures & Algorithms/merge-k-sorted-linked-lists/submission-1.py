# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []

        for i, n in enumerate(lists):
            heapq.heappush(hq, (n.val, i, n))

        dummy = ListNode()
        tail = dummy

        while hq:
            val, i, n = heapq.heappop(hq)

            tail.next = n
            tail = tail.next
            node = n.next

            if node:
                heapq.heappush(hq, (node.val, i, node))
        
        return dummy.next