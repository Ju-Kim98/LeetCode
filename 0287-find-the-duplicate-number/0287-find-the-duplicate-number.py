class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 1
        right = len(nums)-1
        
        while left<right:
            mid = (left+right)//2
            cnt = sum(n <= mid for n in nums)
            
            if cnt > mid:
                right = mid
            else:
                left = mid+1
                
        return left
    
      