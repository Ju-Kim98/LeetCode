class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    
        min_price = float('inf')     #initialize some large value using float('inf')
        profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > profit:
                profit = price - min_price
                
        return profit
                
        
        #Array, Dyanamic Programming