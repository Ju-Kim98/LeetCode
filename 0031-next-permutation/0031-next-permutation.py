class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i = j = len(nums) - 1

        # Step 1: Find the first position `i` from the end where nums[i-1] < nums[i]
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # Step 2: If no such position exists, reverse the list
        if i == 0:  # nums are in descending order
            nums.reverse()
            return

        # Step 3: Find the last "ascending" position `k`
        k = i - 1

        # Step 4: Find the largest element after `k` that is greater than nums[k]
        while nums[j] <= nums[k]:
            j -= 1

        # Step 5: Swap the elements at positions `k` and `j`
        nums[k], nums[j] = nums[j], nums[k]

        # Step 6: Reverse the part of the list after position `k`
        l, r = k + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
