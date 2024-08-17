class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # sliding window
        
        left = 0
        max_len = 0
        char_cnt = {}
        
        for right in range(len(s)):
            char = s[right]
            if char in char_cnt:
                char_cnt[char] += 1
            else:
                char_cnt[char] = 1
                
            while len(char_cnt) > 2:
                left_char = s[left]
                char_cnt[left_char] -= 1
                if char_cnt[left_char] == 0:
                    del char_cnt[left_char]
                left += 1
                
            max_len = max(max_len, right-left+1)
            
        return max_len
                
                
                
                
                
                
                
                
                