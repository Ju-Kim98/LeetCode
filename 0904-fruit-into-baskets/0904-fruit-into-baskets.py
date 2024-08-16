class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        basket = {}
        left = 0
        max_f = 0
        
        for right in range(len(fruits)):
            if fruits[right] in basket:
                basket[fruits[right]] += 1
            else: 
                basket[fruits[right]] = 1
        
            # more than 2 types of f in basket
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            max_f = max(max_f, right-left+1)
        
        return max_f