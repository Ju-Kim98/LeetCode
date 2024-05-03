# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #fast&slow pointer (two pointers)
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next            # one step forward
            fast = fast.next.next       # two step
            if slow == fast:            # when fast pointer meet slow pointer, laps around the cycle and return True
                return True
        return False
    
    #O(n) time, O(1) space
    
    #2nd Set() 안에 node 집어넣을 수 있음
#         x= set()
#         while head is not None:
#             x.add(head)
#             head = head.next
#             if head in x:
#                 return True
#         return False
    
    
    
    