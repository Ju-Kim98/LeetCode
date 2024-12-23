class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # two pointer
        
        l, r = 0, len(height)-1
        max_water = 0
        
        while l<r:
            width = r-l
            h = min(height[l], height[r])
            water = width*h
            max_water = max(max_water, water)
            
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        return max_water