class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        evenL = []
        oddL = []
        
        for i in range(len(nums)):
            if nums[i]%2 == 0:  #짝홀 구분
                evenL.append(nums[i])
            else:
                oddL.append(nums[i])
        
        return evenL + oddL
        