# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pointers = [head for head in lists]
        ans_list = []

        while any(p is not None for p in pointers):
            for j in range(len(pointers)):
                if pointers[j] is not None:
                    ans_list.append(pointers[j].val)
                    pointers[j] = pointers[j].next
        
        ans_list.sort()
        ans = ListNode()
        temp = ans

        for i in ans_list:
            temp.next = ListNode(val=i)
            temp = temp.next
        
        return ans.next