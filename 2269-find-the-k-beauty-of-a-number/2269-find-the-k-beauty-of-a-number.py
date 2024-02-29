class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        num_str = str(num)  # Convert number to string
        count = 0  # Initialize counter for k-beauty
        
        for i in range(len(num_str) - k + 1):
            substring = num_str[i:i+k]  # Extract substring of length k
            divisor = int(substring)  # Convert substring back to integer
            
            if divisor != 0 and num % divisor == 0:  # Check if it's a valid divisor
                count += 1  # Increment counter if conditions are met
                
        return count