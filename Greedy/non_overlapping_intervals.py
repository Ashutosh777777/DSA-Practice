"""
Problem: Non-overlapping Intervals
Platform: LeetCode
Link: https://leetcode.com/problems/non-overlapping-intervals/
Approach: Greedy (maximize non-overlapping intervals by sorting end time)
Time Complexity: O(n log n) due to sorting
Space Complexity: O(1)
"""
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[1])
        i, j, count = 1, 0, 1
        last = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0]>=last:
                last = intervals[i][1]
                count+=1
        return len(intervals)-count
# Sort intervals by their end time to prioritize earlier finishing intervals.
# Select the first interval and track its end as last.
# Iterate and include intervals whose start is ≥ last, updating last and count.
# Minimum removals = total intervals − maximum non-overlapping intervals.