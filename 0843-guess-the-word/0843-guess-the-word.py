# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, words, master):
        """
        :type words: List[Str]
        :type master: Master
        :rtype: None
        """
        import random

        def match(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))
        
        def most_balanced_word(words):
            n = len(words)
            match_counts = [[0] * 7 for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if i != j:
                        match_count = match(words[i], words[j])
                        match_counts[i][match_count] += 1
            # Choose the word with the most balanced match count distribution
            min_max = float('inf')
            best_index = 0
            for i in range(n):
                max_count = max(match_counts[i])
                if max_count < min_max:
                    min_max = max_count
                    best_index = i
            return words[best_index]

        current_words = words[:]
        while current_words:
            guess_word = most_balanced_word(current_words)
            m_count = master.guess(guess_word)
            if m_count == 6:
                return  # Guessed correctly, terminate the function.
            # Filter words based on the guess result
            current_words = [w for w in current_words if match(w, guess_word) == m_count]
