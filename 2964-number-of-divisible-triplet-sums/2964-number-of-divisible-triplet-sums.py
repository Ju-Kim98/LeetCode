class Solution(object):
    def divisibleTripletCount(self, nums, d):
        """
        :type nums: List[int]
        :type d: int
        :rtype: int
        """
        
        # hash table, O(n) time, O(d) space (d: dictionary size)
        
        cnt = 0
        rem_cnt = {}              # track th frequency of each remainder(나머지)
        pair_rem_cnt = {}           # track the frequency of pairs remainder sums
        
        for n in nums:
            rem = n % d
            
            #check if there are pairs with a remainder sum that, 
            #combined with the current number,make a divisible triplet
            target_rem = (d - rem) % d
            if target_rem in pair_rem_cnt:
                cnt += pair_rem_cnt[target_rem]
       
            #update pair_rem_cnt with new pairs formed with the curr remainder
            for r in rem_cnt:
                curr_rem_sum = (r + rem) % d
                if curr_rem_sum not in pair_rem_cnt:
                    pair_rem_cnt[curr_rem_sum] = 0
                pair_rem_cnt[curr_rem_sum] += rem_cnt[r]

            # update rem_cnt with the curr remainder

            if rem not in rem_cnt:
                rem_cnt[rem] = 0
            rem_cnt[rem] += 1
        
        return cnt
    
    
    """
    rem_count: Tracks the frequency of each remainder for numbers seen so far. This is used later to form pairs.
    pair_rem_count: Records the frequency of pairs that sum up to specific remainders. This allows us to check if adding a third number results in a sum divisible by d.
    target_rem: Represents the target remainder needed to achieve a sum divisible by d when combined with the current number.
    """