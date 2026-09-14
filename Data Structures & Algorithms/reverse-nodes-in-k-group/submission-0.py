# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        groupEnd = head
        steps = 0
        while groupEnd and steps < k:
            groupEnd = groupEnd.next
            steps += 1

        if steps < k:
            return head
        
        prev = None
        curr = head
        while curr and curr != groupEnd:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        head.next = self.reverseKGroup(groupEnd, k)
        return prev