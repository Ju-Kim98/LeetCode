class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        hm_char = {}
        hm_word = {}
        
        words = s.split(' ')
        
        if len(words) != len(pattern):
            return False
        
        for c, w in zip(pattern, words):
            if c not in hm_char:
                if w in hm_word:
                    return False
                else:
                    hm_char[c] = w
                    hm_word[w] = c
            else:
                if hm_char[c] != w:
                    return False
        return True
        