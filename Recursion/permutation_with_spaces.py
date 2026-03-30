#User function Template for python3
"""
Problem: Permutation with spaces
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/permutation-with-spaces3627/1
Approach: Recursion and backtracking
Time Complexity: O(2^(n-1) * n log n) due to generating 2^(n-1) combinations and sorting them
"""


class Solution:

    def permutation(self, s):
        res = []
        
        def solve(index, path):
            if index == len(s):
                res.append(path)
                return
            
            solve(index + 1, path + " " + s[index])
            
            solve(index + 1, path + s[index])
        
        solve(1, s[0])
        
        return sorted(res)
    
    
#     At each index, choose add space or no space before the current character
# Use recursion with parameters (index, path) to build all combinations
# Base case: when index == len(s), add the built string to result
# Total combinations = 2^(n-1), finally sort the result before returning