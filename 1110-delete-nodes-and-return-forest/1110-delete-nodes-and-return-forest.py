# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        
        # BFS, O(n) time, O(n) space
        
        s = set(to_delete)
        result = []
        
        def dfs(root, flag):
            if not root:
                return None
            toDelete = (root.val in s)
            root.left = dfs(root.left, toDelete)
            root.right = dfs(root.right, toDelete)
            if not toDelete and flag:
                result.append(root)
            return None if toDelete else root
        
        dfs(root, True)
        return result
        