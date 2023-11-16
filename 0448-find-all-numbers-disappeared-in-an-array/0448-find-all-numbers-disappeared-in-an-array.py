class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # do it w/o extra space and in O(n) runtime => Time: O(n) Space: O(1f7)
        for n in nums:
            i = abs(n)- 1
            nums[i] = -1 * abs(nums[i])
        
        #collect the missing values which are still positive
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result
    
    
#abs() : return absolute val (절댓값)

#34ms
       #return set(range(1, len(nums)+1)) - set(nums) 
    #set()의 time complexity: O(1) or O(n)
        
    

