#User function Template for python3

class Solution:
	def Addition(self, matrixA, matrixB):
		# Code here
		for i in range(len(matrixA)):
		    for j in range(len(matrixB)):
		        matrixA[i][j]+=matrixB[i][j]
        return matrixA