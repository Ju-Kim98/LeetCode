class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        nx = [{} for _ in range(len(t)+1)]
        for i in range(len(t)-1, -1, -1):
            nx[i] = nx[i + 1].copy()
            nx[i][t[i]]= i+1
            
        i = 0
        for c in s:
            if c in nx[i]:
                i = nx[i][c]
            else:
                return False
        
        return True
    
    
    # Dynamic Programming
    
            