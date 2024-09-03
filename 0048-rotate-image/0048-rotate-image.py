class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = (
                    matrix[i][-j - 1],
                    matrix[i][j],
                )
                
#         l, r = 0, len(matrix) - 1

#         while l < r:
#             for i in range(r - l):
#                 top, bottom = l, r

#                 # save the top left
#                 topLeft = matrix[top][l + i]

#                 # move bottom left into top left
#                 matrix[top][l + i] = matrix[bottom - i][l]

#                 # move bottom right into bottom left
#                 matrix[bottom - i][l] = matrix[bottom][r - i]

#                 # move top right into bottom right
#                 matrix[bottom][r - i] = matrix[top + i][r]

#                 # move top left into top right
#                 matrix[top + i][r] = topLeft

#             r -= 1
#             l += 1

                
                
                
                