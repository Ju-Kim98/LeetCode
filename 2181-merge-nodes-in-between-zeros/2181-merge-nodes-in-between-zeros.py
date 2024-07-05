# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # two-pointer, O(n) time, O(1) space
        
        modify = head.next
        nextSum = modify
        
        while nextSum:
            sum = 0
            
            # find the sum of all nodes until encounter 0
            while nextSum.val != 0:
                sum += nextSum.val
                nextSum = nextSum.next
            
            # assign the sum to the cur node's val
            modify.val = sum
            
            # move nextSum to the fisrt non-zero val of the next block
            nextSum = nextSum.next
            
            # move modify to curr node
            modify.next = nextSum
            modify = modify.next
        return head.next
            
            
            
            
            
            
            
            
            
            
            