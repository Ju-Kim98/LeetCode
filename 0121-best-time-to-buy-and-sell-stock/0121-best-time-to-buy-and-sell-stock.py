class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """        
        #binary search (= Sliding Window)
        left = 0    #Buy price
        right = 1   #Sell price
        max_profit = 0
        
        while right < len(prices):
            cur_profit = prices[right] - prices[left]    #current Profit
            if prices[left] < prices[right]:
                max_profit =max(cur_profit,max_profit)
            else:
                left = right
            right += 1
        return max_profit
        
         #Array, Dyanamic Programming / Window sliding algorithm
#         min_price = float('inf')     #initialize some large value using float('inf')
#         profit = 0
        
#         for price in prices:
#             if price < min_price:
#                 min_price = price
#             elif price - min_price > profit:
#                 profit = price - min_price
                
#         return profit
                

      
