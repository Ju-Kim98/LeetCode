class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        bottom = 1
        top = n
        
        while bottom <= top :
            mid = bottom + (top - bottom) // 2  
            coins = mid* (mid + 1) / 2      #등차수열 공식
            if coins == n:      # 동전이 다 참
                return mid
            if coins < n:            #이 경우는 안나옴
                bottom = mid + 1
            else:
                top = mid - 1
        return top
