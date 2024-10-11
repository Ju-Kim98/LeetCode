from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_deque = deque()  # Stores the max elements in the current window
        min_deque = deque()  # Stores the min elements in the current window
        left = 0  # Left pointer of the window
        max_length = 0
        
        for right in range(len(nums)):
            # Maintain max_deque to be decreasing
            while max_deque and nums[right] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[right])
            
            # Maintain min_deque to be increasing
            while min_deque and nums[right] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[right])
            
            # If the difference between max and min exceeds the limit, shrink the window
            while max_deque[0] - min_deque[0] > limit:
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                left += 1
            
            # Calculate the maximum length of the valid subarray
            max_length = max(max_length, right - left + 1)
        
        return max_length
