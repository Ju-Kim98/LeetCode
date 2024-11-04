class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # case1: Sorting, O(nlogn) time
        
        nums = [int(n) for n in str(num)]  # convert the number to a list of digits
        
        odd = sorted([int(n) for n in nums if n % 2 == 1], reverse=True)
        even = sorted([int(n) for n in nums if n % 2 == 0], reverse=True)
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = even.pop(0)
            else:
                nums[i] = odd.pop(0)
                
        return int("".join(map(str, nums)))
    
