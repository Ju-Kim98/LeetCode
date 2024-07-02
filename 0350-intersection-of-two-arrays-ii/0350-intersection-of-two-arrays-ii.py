class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # hash map
        count = {}
        for num in nums1:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        
        # find intersection
        result = []
        for num in nums2:
            if num in count and count[num] > 0:
                result.append(num)
                count[num] -= 1
        return result