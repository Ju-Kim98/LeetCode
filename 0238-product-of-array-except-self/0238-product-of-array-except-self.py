class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # O(n) time, O(1) space
        output = []
        
        mul = 1
        for n in nums:
            output.append(mul)
            mul *= n

        mul = 1
        # for i in range(length-2, -1, -1):   # range(start, stop, step) -> step: -거꾸로 방향, 숫자 만큼, -1 이면 1칸씩 거꾸로
        for i in reversed(range(len(nums))):
            
            output[i] *= mul
            mul *= nums[i]
            
        return output
    
    
    
    


            

