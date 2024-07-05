# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        
        res = [-1,-1]
        pre = head
        cur = head.next
        
        prePos, curPos, firstPos, pos = -1, -1, -1, 0
        
        while cur.next is not None:
            if (cur.val < pre.val and cur.val < cur.next.val) or (cur.val > pre.val and cur.val > cur.next.val):
                prePos = curPos
                curPos = pos
                
                if firstPos == -1:
                    firstPos = pos
                if prePos != -1:
                    if res[0] == -1:
                        res[0] = curPos - prePos
                    else: 
                        res[0] = min(res[0], curPos - prePos)
                    res[1] = pos - firstPos
            pos += 1
            pre = cur
            cur = cur.next
        return res
    
    #O(n) time
            