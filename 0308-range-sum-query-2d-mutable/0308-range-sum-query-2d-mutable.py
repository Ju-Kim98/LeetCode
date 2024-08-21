class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = [[0]*self.n for _ in range(self.m)]
        self.bit = [[0]*(self.n+1) for _ in range(self.m+1)]
        
        for r in range(self.m):
            for c in range(self.n):
                self.update(r, c, matrix[r][c])

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row+1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += diff
                j += (j & -j)
            i += (i & -i)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self._sum(row2, col2) - self._sum(row2, col1-1) - self._sum(row1-1, col2) + self._sum(row1-1, col1-1)
        
    def _sum(self, row, col):
        summ = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                summ += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return summ


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)