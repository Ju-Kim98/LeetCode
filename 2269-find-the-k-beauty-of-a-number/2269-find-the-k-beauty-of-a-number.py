class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        num_str = str(num) #convert num to string (정수를 문자열로  )
        count = 0  
        l = len(num_str)
        
        for i in range(l - k + 1):
            substring = num_str[i:i+k]  # 길이 k인 (index i부터 i+k) substring 
            divisor = int(substring)  #substring 배열을 정수로
            
            if divisor != 0 and num % divisor == 0: 
                count += 1 
                
        return count