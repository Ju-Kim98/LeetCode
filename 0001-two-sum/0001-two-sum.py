class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # hash map - O(n) time, O(n) space
        
        hm = {}
        for i, num in enumerate(nums):
            k = target - num
            if k in hm:
                return [hm[k], i]
            hm[num] = i