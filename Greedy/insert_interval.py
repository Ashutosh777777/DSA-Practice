"""
Problem: Insert Interval
Platform: LeetCode
Link: https://leetcode.com/problems/insert-interval/
Approach: Greedy (linear scan with merging)
Time Complexity: O(n)
Space Complexity: O(n) for result
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res
# Add all intervals that end before the new interval (no overlap).
# Merge all overlapping intervals by updating the new interval’s start and end.
# Append the merged new interval to the result.
# Add the remaining intervals that start after the merged interval.