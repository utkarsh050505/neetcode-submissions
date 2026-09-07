# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node pointing to the head
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both pointers until fast reaches the last node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        # slow is now right before the node to be deleted
        slow.next = slow.next.next

        # Return the actual head, which is dummy.next
        return dummy.next