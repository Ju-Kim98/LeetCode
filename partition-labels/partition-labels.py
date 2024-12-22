class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        dict = {c: i for i, c in enumerate(s)}
        ans = []
        j = partition = 0
        
        for i, c in enumerate(s):
            j = max(j, dict[c])
            if i == j:
                ans.append(i-partition+1)
                partition = i+1
        return ans