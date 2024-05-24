class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        
        h_set = set()
        l = len(nums)
        
        for i in range(l):
            j = i-k
            if nums[i] in h_set:
                return True
            h_set.add(nums[i])
            if len(h_set) > k:
                h_set.remove(nums[j])
        return False
        