class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        normalized = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        
        words = normalized.split()
        
        word_cnt = defaultdict(int)
        banned_word = set(banned)
        
        for w in words:
            if w not in banned_word:
                word_cnt[w] += 1
                
        res= max(word_cnt.items(), key=operator.itemgetter(1))[0]
        
        return res
        
       