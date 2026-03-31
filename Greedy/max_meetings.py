
"""
Problem: N Meetings in One Room (Return Meeting Indices)
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
Approach: Greedy (sort by end time + track indices)
Time Complexity: O(n log n) due to sorting
Space Complexity: O(n) for storing meetings and result
"""

from typing import List

class Solution:
    def maxMeetings(self, N: int, S: List[int], F: List[int]) -> List[int]:
        arr = [[S[i], F[i], i+1] for i in range(N)]
        
        arr.sort(key=lambda x: x[1])
        
        res = []
        res.append(arr[0][2])
        
        last = arr[0][1]
        
        for i in range(1, N):
            if arr[i][0] > last:
                last = arr[i][1]
                res.append(arr[i][2])
        
        res.sort()   
        
        return res
    
# Store meetings as (start, end, index) and sort them by end time.
# Select the first meeting, then greedily pick meetings whose start time is greater than the last selected end time.
# Store the indices of selected meetings while maintaining the greedy choice.
# Sort the final list of indices before returning (as required by the problem).