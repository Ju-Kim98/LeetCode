class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        # bottom-up DP
        
        # dp[i]: list w/ no substrings have been validated as segmentable yet
        dp = [False]*len(s) 
        
        for i in range(len(s)):
            for word in wordDict:
                if i < len(word) - 1:
                    continue
                    
                if i == len(word) - 1 or dp[i-len(word)]:
                    if s[i-len(word) + 1 : i+1] == word:
                        dp[i] = True
                        break
                        
        return dp[-1]
                    
        