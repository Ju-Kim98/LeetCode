class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
#         #sort O(nlogn)
#         nums1.sort()
#         nums2.sort()
        
#         #initializing pointers
#         i=0;
#         j=0;
        
#         inter_set = set()
        
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] == nums2[j]:
#                 #add to set if same ele
#                 inter_set.add(nums1[i])
#                 i+=1
#                 j+=1
#             elif nums1[i]<nums2[j]:
#                 i+=1
#             else: 
#                 j+=1
                
#         return list(inter_set)
    
    
    #sort를 안 쓰는 방법
    
    # Use a set for constant time look-up
        nums1_set = set(nums1)
        result_set = set()

        # Check each element in nums2
        for num in nums2:
            if num in nums1_set:
                result_set.add(num)

        # Convert the result set to a list
        return list(result_set)