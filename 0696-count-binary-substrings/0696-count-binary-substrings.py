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
    
   # Time Complexity : O(N), where N is the length of given string.
   # Space Complexity : O(1), since only constant space is being used.