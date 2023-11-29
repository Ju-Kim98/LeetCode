class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        answer = [0] * n
        c_positions = [i for i in range(n) if s[i] == c]

        # Iterate through each character in the string
        for i in range(n):
            # Compute the minimum distance to any occurrence of c
            answer[i] = min([abs(i - pos) for pos in c_positions])

        return answer