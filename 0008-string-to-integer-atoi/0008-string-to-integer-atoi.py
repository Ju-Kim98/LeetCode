class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Constants for 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Step 1: Strip leading whitespace
        s = s.lstrip()
        
        if not s:
            return 0
        
        # Step 2: Determine the sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]  # Strip the sign for further processing
        elif s[0] == '+':
            s = s[1:]  # Strip the sign for further processing
        
        result = 0
        
        # Step 3: Convert characters to integer
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break  # Stop converting when a non-digit is encountered
        
        # Step 4: Apply the sign and clamp to 32-bit integer range
        result *= sign
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
