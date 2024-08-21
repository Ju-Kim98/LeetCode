class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # two pointer
        # 0-0, 1-1, 2-F, 3-F, 4-F, 5-F, 6-9, 7-F, 8-8, 9-6
        
        rotated_digits = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        left, right = 0, len(num)-1
        
        while left <= right:
            if num[left] not in rotated_digits or rotated_digits[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True