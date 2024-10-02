class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        res = []
        
        i, j = 0, len(numbers)-1
        
        while i < j:
            Sum = numbers[i] + numbers[j]
            
            if Sum == target:
                return [i+1, j+1]  #since given array is 1-indexed, +1
            elif Sum < target:
                i += 1
            else:
                j -= 1
                
        return res
        