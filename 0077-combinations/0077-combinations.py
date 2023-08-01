class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):        #backtrack: 막히면 다시 돌아가서 찾는거
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()
                
        #12,13,14 라인이 for문 안에서 돌아가면 안됨(실수조심)
        output = []
        backtrack()
        return output