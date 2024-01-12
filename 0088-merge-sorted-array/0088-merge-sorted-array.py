class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #O(n)  (Sort는 nlogn)
    
        # pointer 
        p1 = m - 1
        p2 = n - 1
        pm = m + n - 1

        # nums1, nums2 merge
        while p1 >= 0 and p2 >= 0:
            if nums1[p1]>nums2[p2]:
                nums1[pm] = nums1[p1]
                p1 -= 1                 #p1 = p1-1
            else:  #nums1[p1]<nums2[p2]
                nums1[pm] = nums2[p2]
                p2 -= 1
            pm -= 1

        # put nums2 to nums1
        while p2 >= 0:
            nums1[pm] = nums2[p2]
            p2 -= 1
            pm -= 1

        