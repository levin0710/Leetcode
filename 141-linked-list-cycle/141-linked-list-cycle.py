# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next
            
            if fast is None:
                return False
            fast = fast.next
                
            
                
            if slow == fast:
                return True
                
            
            
            
        return False
        