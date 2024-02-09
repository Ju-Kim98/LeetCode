class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Palindrome(대칭), two pointers O(n) time
        
        # to check if a substring is a palindrome
        def check_palindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Check by removing one character (either left or right)
                return check_palindrome(s, left + 1, right) or check_palindrome(s, left, right - 1)
            left, right = left + 1, right - 1
        return True
    
