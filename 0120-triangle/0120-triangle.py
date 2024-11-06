class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # bottom up DP
        
        for row in range(1, len(triangle)):
            for col in range(row + 1): 
                m = math.isinf      #set m is an infinity value
                if col > 0:
                    m = triangle[row-1][col-1]
                if col < row:
                    m = min(m, triangle[row-1][col])
                triangle[row][col] += m
                
        return min(triangle[-1])