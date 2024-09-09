class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        def check(s, word):
            i, j = 0, 0
            while i<len(s) and j<len(word):
                if s[i] != word[j]:
                    return False
                len_s = 1
                while i+len_s < len(s) and s[i+len_s] == s[i]:
                    len_s += 1
                len_w = 1
                while j+len_w < len(word) and word[j+len_w] == word[j]:
                    len_w += 1
                    
                if len_s < 3 and len_s != len_w:
                    return False
                if len_s >= 3 and (len_w > len_s or len_w < 1):
                    return False
                
                i += len_s
                j += len_w
                
            return i == len(s) and j == len(word)
        
        count = 0
        for word in words:
            if check(s, word):
                count += 1
        return count