# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        # BFS, O(n) time, O(n) space
        
        q = [root]
        res = []
        
        while len(q):
            q_len = len(q)
            q_sum = 0
            for i in range(len(q)):
                curr = q.pop(0)
                q_sum += curr.val
                
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(float(q_sum) / q_len)
            
            
        return res