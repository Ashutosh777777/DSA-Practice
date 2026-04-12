"""
Problem: Partition to K Equal Sum Subsets
Platform: LeetCode
Link: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
Approach: Backtracking with pruning
Time Complexity: O(k * 2^n) in worst case (pruned heavily in practice)
Space Complexity: O(n) recursion + used array
"""
#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
		# code here
		n = len(arr)
		t = [[0]*(target+1) for _ in range(n+1)]
		
		for i in range(n+1):
		    t[i][0] = 1
		
		for i in range(1, n+1):
		    for j in range(target+1):
		        if arr[i-1]<=j:
		            t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]
		        else:
		            t[i][j] = t[i-1][j]
		return t[n][target]
# Check if total sum is divisible by k; each subset must sum to target = total/k.
# Sort in descending order to place larger elements first (better pruning).
# Use backtracking to build subsets, marking elements as used.
# Once a subset reaches target, recursively form the remaining k-1 subsets.