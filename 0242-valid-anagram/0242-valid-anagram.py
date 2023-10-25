class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # case1: Sort 두 array를 알파벳순으로 sort하고 서로 요소가 같은지 확인하기
        return sorted(s) == sorted(t)  #O(nlogn)

    
    """  
    #case1: with two count array
        return Counter(s) == Counter(t)
    
        if len(s) != len(t):
            return False 
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countS.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
            
        return True
"""
        
    
    
    
    # case1) 
    # case2)
    