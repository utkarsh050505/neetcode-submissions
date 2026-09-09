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
        d = {}
        curr = head

        dummy = Node(0)
        temp = dummy

        while curr:
            temp.next = Node(curr.val)
            temp = temp.next
            curr = curr.next
        
        curr = head
        temp = dummy.next

        while curr:
            d[curr] = temp
            curr = curr.next
            temp = temp.next

        
        for i in d:
            if i.random:
                d[i].random = d[i.random]
            else:
                d[i].random = None
        
        return dummy.next