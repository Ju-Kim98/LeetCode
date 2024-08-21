class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def canPartition(mid):
            cur_sum = 0
            required_subarrays = 1
            
            for num in nums:
                if cur_sum + num > mid:
                    required_subarrays += 1
                    cur_sum = num
                    
                    if required_subarrays > k: 
                        return False
                else: 
                    cur_sum += num
            return True
        
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left+right)//2
            if canPartition(mid):
                right = mid-1
            else:
                left = mid+1
        return left