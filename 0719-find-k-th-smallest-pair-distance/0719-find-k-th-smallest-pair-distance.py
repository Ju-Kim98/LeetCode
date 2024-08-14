class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        
        def helper(dist): 
            # count total num of pairs w/ diff <= dist
            left = 0
            res = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > dist:
                    left += 1             
                res += right - left
            return res
            
        left, right = 0, max(nums)
        while left < right:
            mid = left + ((right-left)//2)
            pairs = helper(mid)
            if pairs >= k:
                right = mid
            else:
                left = mid+1
        return right