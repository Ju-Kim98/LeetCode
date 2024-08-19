class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[List[int]]
        """
        res = []
        prev = lower-1  
        
        for i in range(len(nums)+1):
            curr = nums[i] if i<len(nums) else upper +1
            if prev + 1 <= curr -1:
                res.append([prev+1, curr-1])
            prev = curr
            
        return res
    