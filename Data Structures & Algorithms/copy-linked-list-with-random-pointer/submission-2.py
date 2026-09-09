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
        curr = head

        while curr:
            nxt = curr.next
            curr.next = Node(x=curr.val, next=nxt)
            curr = nxt
        
        curr = head

        while curr:
            if curr.next:
                curr.next.random = curr.random.next if curr.random else None
                curr = curr.next.next
        
        curr = head
        dummy = Node(0)
        copy_curr = dummy

        while curr:
            copy_curr.next = curr.next
            copy_curr = copy_curr.next

            curr.next = curr.next.next
            curr = curr.next
        
        return dummy.next