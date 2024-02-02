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

    # 오른쪽에 있는 nums[i], nums[lastNonZeroFoundAt]를 평가합니다. 이는 nums[i]와 nums[lastNonZeroFoundAt]의 값이 포함된 튜플을 생성합니다. 이 단계에서 이 두 요소의 현재 값이 임시로 저장됩니다, 이는 교환을 가능하게 합니다.

# nums[lastNonZeroFoundAt]에 할당하고, 튜플의 두 번째 요소를 nums[i]에 할당합니다. 이 할당은 동시에 발생합니다, 즉 nums[lastNonZeroFoundAt]와 nums[i]는 동시에 새로운 값으로 업데이트됩니다.