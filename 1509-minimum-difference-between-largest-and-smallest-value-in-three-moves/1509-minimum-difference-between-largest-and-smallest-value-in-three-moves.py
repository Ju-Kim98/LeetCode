class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)
        
        # if array has 4 or fewer elements, return 0
        if l <= 4:
            return 0
        
        nums.sort()
        
        min_diff = float("inf")
        
        # 4 cases to compute the minimum difference
        for left in range(4):
            right = l - 4 + left
            min_diff = min(min_diff, nums[right]-nums[left])
            
        return min_diff