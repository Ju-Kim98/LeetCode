class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])  #create copy
                return
            if total > target or i == len(candidates):
                return
            #include candidates[i]
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            cur.pop()
            
            #skip candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, cur, total)
        dfs(0,[], 0)
        return res