class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        
        def build_prefix_dict(words):
            prefix_dict = defaultdict(list)
            for word in words:
                for i in range(len(word)):
                    prefix_dict[word[:i]].append(word)
            return prefix_dict

        def is_valid_square(square, word, index):
            for i in range(index):
                if square[i][index] != word[i]:
                    return False
            return True

        def backtrack(index, current_square):
            if index == len(words[0]):
                result.append(current_square[:])
                return
            
            # Form the prefix for the next potential word in the square
            prefix = ''.join([word[index] for word in current_square])
            for candidate in prefix_dict[prefix]:
                if is_valid_square(current_square, candidate, index):
                    current_square.append(candidate)
                    backtrack(index + 1, current_square)
                    current_square.pop()

        # Main function body starts here
        prefix_dict = build_prefix_dict(words)
        result = []
        for word in words:
            backtrack(1, [word])
        return result