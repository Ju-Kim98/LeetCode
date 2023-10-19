class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
       
        HashSet = set()  #set: 집합, 중복x, 순서x / O(1) time
        for n in nums:      #O(n)
            if n in HashSet:
                return True
            HashSet.add(n) 
        else:
            return False
        
        
         
        
    
        
        """
        
        #sorting을 해서 그 리스트를 for룹 옆에있는 숫자 비교
        #sort func O(nlogn)
        nums.sort(nums): 
        for n in range(nums):
            if n == n+1:
                return True
                n++
            else:
                return False 
                
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
                
        d = {}
        for ele in nums:
            d[ele] = d.get(ele,0) + 1
        
        """
            