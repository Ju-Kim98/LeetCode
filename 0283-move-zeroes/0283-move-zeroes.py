class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        zero_move = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i>zero_move:
                    nums[zero_move], nums[i] = nums[i], nums[zero_move]
                zero_move += 1
                
                