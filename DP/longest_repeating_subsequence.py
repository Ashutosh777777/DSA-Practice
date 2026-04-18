"""
Problem: Longest Repeating Subsequence
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1
Approach: LCS(s, s) with i != j constraint
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""
#User function Template for python3

class Solution:
	def LongestRepeatingSubsequence(self, s):
		# Code here
		n= len(s)
		
		t = [[0]*(n+1) for _ in range(n+1)]
		
		for i in range(1, n+1):
		    for j in range(1, n+1):
		        if s[i-1]==s[j-1] and i!=j:
		            t[i][j] = 1 + t[i-1][j-1]
		        else:
		            t[i][j] = max(t[i-1][j], t[i][j-1])          
		return t[n][n]
# Treat the string as two copies and compute LCS between them.
# Add constraint i != j to avoid matching same index.
# If characters match at different indices → include in subsequence.
# Result gives longest subsequence that appears at least twice.