class Solution:
    def printTillN(self, N):
    	#code here 
    	def solve(n):
        	if n>N:
        	    return 
            print(n, end=" ")
            return solve(n+1)
        return solve(1)