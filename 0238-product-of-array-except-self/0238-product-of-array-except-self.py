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
        # for i in range(length-2, -1, -1):
        for i in reversed(range(len(nums))):
            
            output[i] *= mul
            mul *= nums[i]
            
        return output
    
    
    
    


            

