class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sliding window
        res = 0
        cur_char = {}
        i = 0
        
        for j in range(len(s)):
            if s[j] in cur_char:
                i = max(cur_char[s[j]], i)
            res = max(res, j-i+1)
            cur_char[s[j]] = j+1
        return res