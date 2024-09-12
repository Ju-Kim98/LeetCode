class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        hash_map = {}
        prefix_sum = [0]
        ans = float('-inf')

        for i, num in enumerate(nums):
          if num not in hash_map or prefix_sum[hash_map[num]]>prefix_sum[-1]:
            hash_map[num] = i
          curr_sum = prefix_sum[-1]+num
          prefix_sum.append(curr_sum)

          if k+num in hash_map:
            index = hash_map[k+num]
            ans = max(ans, curr_sum - prefix_sum[index])

          if -k+num in hash_map:
            index = hash_map[-k+num]
            ans = max(ans, curr_sum - prefix_sum[index])
        return 0 if ans == float('-inf') else ans

