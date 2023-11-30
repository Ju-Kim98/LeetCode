class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
      
        res, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                res += min(prev, cur)
                prev = cur
                cur = 1
            else:
                cur += 1
        res += min(prev, cur)
        return res
    
   # Time: O(N), Space: O(1) 

#왼쪽 오른쪽으로 나눠서 해도 될듯