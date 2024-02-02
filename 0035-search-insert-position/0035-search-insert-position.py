class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
       
    # O(logn) time
        
        left = 0;
        right = len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left=mid+1
                #return left
            else:
                right = mid-1
                #return right
        return left
            
            #target이 없는 경우 
            
        
        
        