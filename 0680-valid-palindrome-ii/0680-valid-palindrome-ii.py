class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # Palindrome(대칭), two pointers O(n) time : helper function is O(n) time, main func is also O(n), but helper function is for checking, so final time complexity is O(n) time
        
        # helper function: to check if a substring is a palindrome 
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
    
        # without create new function
        # left = 0
        # right = len(s) - 1
        # while start <= end:
        #     if s[start] == s[end]:
        #         start += 1
        #         end -= 1
        #     else:
        #         s1=s[:start]+s[start + 1:]
        #         s2=s[:end]+s[end + 1:]
        #         if s1[::-1] == s1 or s2[::-1] == s2:
        #             return True
        #         else:
        #             return False

        # return True
