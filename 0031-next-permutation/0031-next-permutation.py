class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        pivot = n - 1
        
        # find the largest index 'pivot' such that nums[pivot-1] < nums[pivot]
        while pivot > 0 and nums[pivot-1] >= nums[pivot]:
            pivot -= 1
            
        # if such pivot is found, find the rightmost element that exceeds nums[pivot-1] and wap them
        if pivot > 0:
            i = n-1
            while nums[i] <= nums[pivot-1]:
                i -= 1
            nums[pivot-1], nums[i] = nums[i], nums[pivot-1]
            
        # reverse the suffix starting at 'pivot'
        left, right = pivot, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        