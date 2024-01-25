class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # O(n)
        #stack to track opening brackets
        stack = []

        #hash mapping
        h_map = {"]":"[", "}":"{", ")":"("}
        
        for char in s:
            if char in h_map.values():
                stack.append(char)
            elif char in h_map.keys():
                if stack == [] or h_map[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []