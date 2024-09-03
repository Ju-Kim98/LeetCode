class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Edge case: if either num1 or num2 is "0", return "0"
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize a result list to store the multiplication results
        result = [0] * (len(num1) + len(num2))
        
        # Reverse both strings to simplify the calculation from right to left
        num1, num2 = num1[::-1], num2[::-1]
        
        # Perform multiplication digit by digit
        for i in range(len(num1)):
            for j in range(len(num2)):
                # Multiply the digits and add to the corresponding position in result
                mul = int(num1[i]) * int(num2[j])
                result[i + j] += mul
                
                # Handle carry
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        # The result list now contains the digits in reverse order
        # Reverse it back and convert to a string, stripping any leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        # Convert the list of digits to a string and return
        return ''.join(map(str, result[::-1]))
        