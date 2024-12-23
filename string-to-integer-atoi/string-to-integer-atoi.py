class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # constants for 32-bit signed integer limits
        int_max = 2**31 - 1
        int_min = -2**31
        
        # strip leading withespace(공백제거)
        s = s.lstrip()              # lstrip: 문자를 왼쪽에서 제거
        if not s:
            return 0
        
        # sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]  # string 제일 앞에 두기
        elif s[0] == '+':
            s = s[1:]
            
        res = 0
        
        # convert char to int => isdigit
        for char in s:
            if char.isdigit():
                res = res*10 + int(char)
            else:
                break    # stop converting when non-digit is encountered
        
        res *= sign
        
        if res < int_min:
            return int_min
        if res > int_max:
            return int_max
        
        return res
        
    