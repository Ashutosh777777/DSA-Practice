#User function Template for python3
"""
Problem: Maximum Meetings in One Room
Platform: GFG
Link: https://www.geeksforgeeks.org/problems/maximum-meetings-in-one-room/1
Approach: Greedy (sort by meeting end time)
Time Complexity: O(n log n) due to sorting
Space Complexity: O(n) for storing meetings
"""
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        # code here
        arr = [[start[i], end[i]] for i in range(len(start))]
        
        arr.sort(key=lambda x: x[1])
        
        i, j, count = 1, 0, 1
        last = arr[0][1]
        for i in range(1, len(arr)):
            if arr[i][0]>last:
                last = arr[i][1]
                count+=1
        return count
    
# Pair start and end times, then sort meetings by their end time.
# Always pick the meeting that finishes earliest to maximize remaining time.
# Iterate and select a meeting only if its start time is greater than the last selected meeting’s end time.
# This greedy choice ensures the maximum number of non-overlapping meetings.