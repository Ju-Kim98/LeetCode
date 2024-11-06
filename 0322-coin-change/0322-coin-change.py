class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # Bottom-up DP
        
        dp = [float('inf')]*(amount+1)       #assume that you have an infinite number of each kind of coin
        dp[0] = 0
        
        for c in coins:
            for i in range(c, amount+1):
                dp[i] = min(dp[i], dp[i-c]+1)
        
        return dp[amount] if dp[amount] != float('inf') else -1