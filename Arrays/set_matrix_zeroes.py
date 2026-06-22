class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        h = []
        k = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    h.append(i)
                    k.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in h or j in k:
                    matrix[i][j] = 0
        return matrix