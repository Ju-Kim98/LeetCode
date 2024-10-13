class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        res = []
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        while top <= bottom and left <= right:
            # TopLeft to TopRight
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # TopRight to BottomRight
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # BottomRight to BottomLeft
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # BottomLeft to TopLeft
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res
