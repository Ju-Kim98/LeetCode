class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
    # O(n^2) Time sol
    
        n = len(s)
        answer = [0] * n
        
        #ind = [i for i in range(n) if s[i] == c]  #index position of c

        #for i in range(n):
        #    answer[i] = min([abs(i - j) for j in ind])  

        #return answer

    # O(n) Time sol
      
        left = [float('inf')] *n
        right =[float('inf')] *n
           
        temp = float('inf')
        for i in range(n):
            if s[i] == c:
                temp = 0
            left[i] = temp
            temp += 1

        #temp = float('inf')
        for i in reversed(range(n)):
            if s[i] == c:
                temp = 0
            right[i] = temp
            temp += 1

        for i in range(n):
            answer[i] = min(left[i], right[i])

        return answer
    