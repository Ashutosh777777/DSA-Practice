class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        
        s = 0
        e = m*n-1

        while s<=e:
            mid = (s+e)//2
            row = mid//n
            col = mid%n

            val = matrix[row][col]
            if val==target:
                return True
            elif val>target:
                e = mid-1
            else:
                s = mid+1
        return False