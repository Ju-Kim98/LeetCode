class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         #Count O(n) time
#         positive = 0
#         negative = 0
        
#         for n in nums:
#             if n > 0:
#                 positive +=1
#             elif n < 0:
#                 negative +=1
#         return max(positive, negative)
        
        
        #Binary Search O(log(n)) time

        left = 0
        right = len(nums) - 1
        
        if nums[left] > 0 or nums[right] < 0:
            return len(nums)
            
        if nums[left] == 0 and nums[right] == 0:
            return 0

        while left <= right:
            
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid+1
            elif nums[mid] > 0:
                right = mid-1    
            else:
                nums.remove(0)
                right -= 1
                
        negative = left
        positive = len(nums)-left

        return max(negative,positive)
