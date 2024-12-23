class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # hash map - O(n) time, O(n) space
        hm = {}
        for i, n in enumerate(nums):
            k = target - n
            if k in hm:
                return [hm[k], i]
            hm[n] = i