class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
       
    #O(n) time
    
        zero_move = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_move], nums[i] = nums[i], nums[zero_move]     #두 배열의 요소 값 swap
                zero_move += 1
                
    #[0,1,0,3,12]
    #i = 0, nums[0]=1 != 0 -> 0, 1 = 1, 0 
                