# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """     
        
        
        dummy = ListNode()
        curr = dummy
        carry = 0                   #반올림 
        
        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0
            
            #new digit
            val = val_1 + val_2 + carry
            carry = val//10
            val = val%10
            curr.next = ListNode(val)
            
            #update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
    
    
  
        