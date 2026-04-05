"""
Problem: Minimum Platforms
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
Approach: Greedy (two pointers / sweep line on arrival & departure)
Time Complexity: O(n log n) due to sorting
Space Complexity: O(1)
"""
class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        
        arr.sort()
        dep.sort()
        
        p = 0
        mp = 0
        i = j = 0
        n = len(arr)
        while i<n and j<n:
            if arr[i]<=dep[j]:
                p+=1
                i+=1
            else:
                p-=1
                j+=1
            mp = max(p, mp)
        return mp
# Sort arrival and departure times separately.
# Use two pointers to simulate trains arriving and leaving.
# If a train arrives before the earliest departure, increase platform count; else decrease it.
# Track the maximum platforms needed at any time during traversal.