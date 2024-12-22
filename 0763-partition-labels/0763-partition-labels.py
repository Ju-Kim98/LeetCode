class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
        dict = {c: i for i, c in enumerate(s)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(s):
            j = max(j, dict[c])
            if i == j:
                ans.append(i-anchor+1)
                anchor = i + 1
                
        return ans