class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        open_parentheses = deque()
        result = []
        
        for curr_char in s:
            if curr_char == "(":
                open_parentheses.append(len(result))
            elif curr_char == ")":
                start = open_parentheses.pop()
                result[start:] = result[start:][::-1]
            else:
                result.append(curr_char)
                
        return "".join(result)