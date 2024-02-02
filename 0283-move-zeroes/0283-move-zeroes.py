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
                
   

#memo
# 오른쪽 nums[i], nums[zero_move] => nums[i]와 nums[zero_move]의 값이 포함된 튜플을 생성 후 두 요소의 현재 값이 임시로 저장-
# 왼쪽 nums[zero_move]과 튜플의 두 번째 요소를 nums[i]에 동시에 할당