"""
Problem: Minimum Insertions and Deletions to convert s1 to s2
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1
Approach: LCS-based transformation
Time Complexity: O(n * m)
Space Complexity: O(n * m)
"""
#User function Template for python3
class Solution:
	def minOperations(self, s1, s2):
		# code here
		n = len(s1)
		m = len(s2)
		
		t = [[0]*(m+1) for _ in range(n+1)]
		for i in range(1, n+1):
		    for j in range(1, m+1):
		        if s1[i-1]==s2[j-1]:
		            t[i][j] = 1 + t[i-1][j-1]
		        else:
		            t[i][j] = max(t[i-1][j], t[i][j-1])
		
		return (n+m) - 2*(t[n][m])
# Compute LCS of both strings.
# Characters in LCS don’t need any operation.
# Delete remaining characters from s1 and insert missing ones from s2.
# Total operations = (n − LCS) + (m − LCS).