class Solution(object):
    def sameEndSubstringCount(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(s)
        char_set = set(s)
        count = {c: [0] * (n + 1) for c in char_set}
        for i, a in enumerate(s, 1):
            for c in char_set:
                count[c][i] = count[c][i - 1]
            count[a][i] += 1
        ans = []
        for l, r in queries:
            t = r - l + 1
            for c in char_set:
                x = count[c][r + 1] - count[c][l]
                t += x * (x - 1) // 2
            ans.append(t)
        return ans