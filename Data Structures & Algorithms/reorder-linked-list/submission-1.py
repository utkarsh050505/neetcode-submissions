# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        temp = head

        while temp.next != slow:
            temp = temp.next
        
        temp.next = None

        prev = None
        curr = slow
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        l2 = prev
        dummy = ListNode()

        while l1 and l2:
            nxt1 = l1.next
            nxt2 = l2.next

            l1.next = l2      
            if not nxt1:     
                break
            l2.next = nxt1 
            
            l1 = nxt1
            l2 = nxt2