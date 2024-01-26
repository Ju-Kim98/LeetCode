class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # O(n)
        #stack to track opening brackets
        stack = []

        #hash mapping - for quick lookups to match pairs
        h_map = {"]":"[", "}":"{", ")":"("}  # values:keys
        
        for char in s:
            # if cur char is opening, append to stack
            if char in h_map.values():
                stack.append(char)
                
            # if cue char is closing,    
            elif char in h_map.keys():
                #stack == [] stack is empty, closed로만 이뤄져있음
                #
                if stack == [] or h_map[char] != stack.pop():   
                    return False
            else:
                return False
            
        return stack == []  #return true when stack is empty