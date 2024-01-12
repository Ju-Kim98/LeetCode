class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
    
        # Initialize pointers for nums1, nums2, and the merged array
        p1 = m - 1
        p2 = n - 1
        pm = m + n - 1

        # Merge nums1 and nums2 from the end to the beginning
        while p1 >= 0 and p2 >= 0:
            if nums1[p1]>nums2[p2]:
                nums1[pm] = nums1[p1]
                p1 -= 1                 #p1 = p1-1
            else:               #nums1[p1]<nums2[p2]
                nums1[pm] = nums2[p2]
                p2 -= 1
            pm -= 1

        # If there are remaining elements in nums2, copy them to nums1
        while p2 >= 0:
            nums1[pm] = nums2[p2]
            p2 -= 1
            pm -= 1

        #final sorted array should not be returned by the function
        