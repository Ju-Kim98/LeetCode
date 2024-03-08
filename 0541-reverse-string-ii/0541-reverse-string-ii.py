class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        #two pointers 
        
        new_list = list(s)  #change string to list 
        
        for start in range(0, len(s), 2*k):
            left = start
            right = min(start + k - 1, len(s) - 1)
            
            while left < right:
                new_list[left], new_list[right] = new_list[right], new_list[left]
                left += 1
                right -= 1
        
        return ''.join(new_list)      # Join the list back into a string

        
        #String: solution: O(n) time, O(n) space
        # l = list(s)   
        # for i in range(0,len(l),2*k):
        #     l[i:i+k] = reversed(l[i:i+k])   
        # return "".join(l)
    
