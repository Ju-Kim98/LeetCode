class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def canEat(k):
            hours = 0
            for pile in piles:
                hours += (pile + k -1)//k  #math.ceil(pile/k)   
            return hours <= h

        left = 1
        right = max(piles)

        while left <= right:
            mid = (left+right)//2
            if canEat(mid):
                right = mid-1
            else:
                left = mid+1
        return left
    
    

    
    
    
    