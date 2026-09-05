class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Start both pointers at the head
        slow = head
        fast = head

        # As long as fast and fast.next are valid nodes, keep moving
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            # If they meet, a cycle exists
            if fast == slow:
                return True
        
        # If fast reaches the end, there is no cycle
        return False