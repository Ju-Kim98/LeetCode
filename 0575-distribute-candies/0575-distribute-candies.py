class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        #ex) input = {1,1,2,3}
        
        CandyType = set(candyType)   #CandyType = {1,2,3}
          
        
        return min(len(CandyType),len(candyType)//2) #3 또는 4/2=2 중 작은값 => 2
         