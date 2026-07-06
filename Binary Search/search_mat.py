class Solution:
	def matSearch(self, mat, x):
		# Complete this function
		i = 0
		j = len(mat[0])-1
		
		while len(mat)>i>=0 and len(mat[0])>j>=0:
		    if mat[i][j] == x:
		        return True
		    elif mat[i][j] > x:
		        j-=1
		    else:
		        i+=1
		return False