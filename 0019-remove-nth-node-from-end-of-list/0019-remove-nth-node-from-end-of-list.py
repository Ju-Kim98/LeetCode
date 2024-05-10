# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
    
        left = right = head
        
        for i in range(n):
            right = right.next
            
        if not right:
            return left.next
        
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head
        
      
        
        