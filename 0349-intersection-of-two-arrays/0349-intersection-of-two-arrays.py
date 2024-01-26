class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        #hash set 방법, O(n) time
    
        inter_set = set()         # hash set: 겹치는거 모아두기

        # Check each element in nums2
        for num in nums2:
            if num in nums1:        #nums2에 있는 num이nums1에 존재할 때, inter_set에 add
                inter_set.add(num)

        #list로 출력하기
        return list(inter_set)
        
        #returrn inter_set
        
                
#         #Using Sort: O(nlogn) time
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
        
        
        
