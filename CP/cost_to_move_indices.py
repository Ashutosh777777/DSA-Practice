"""
Problem: Minimum Cost to Move Between Indices
Platform: LeetCode Weekly Contest 500
Link: https://leetcode.com/contest/weekly-contest-500/problems/minimum-cost-to-move-between-indices/
Approach: Precompute Closest Index + Prefix Sum Costs
Time Complexity: O(n + q)
Space Complexity: O(n)
"""

class Solution(object):
    def minCost(self, nums, queries):
        n = len(nums)

        closest = [-1] * n

        for i in range(n):
            if i == 0:
                closest[i] = 1
            elif i == n - 1:
                closest[i] = n - 2
            else:
                left = nums[i] - nums[i - 1]
                right = nums[i + 1] - nums[i]

                if left <= right:
                    closest[i] = i - 1
                else:
                    closest[i] = i + 1

        rightCost = [0] * (n - 1)

        for i in range(n - 1):
            if closest[i] == i + 1:
                rightCost[i] = 1
            else:
                rightCost[i] = nums[i + 1] - nums[i]

        leftCost = [0] * n

        for i in range(1, n):
            if closest[i] == i - 1:
                leftCost[i] = 1
            else:
                leftCost[i] = nums[i] - nums[i - 1]

        prefRight = [0] * n
        for i in range(n - 1):
            prefRight[i + 1] = prefRight[i] + rightCost[i]

        prefLeft = [0] * n
        for i in range(1, n):
            prefLeft[i] = prefLeft[i - 1] + leftCost[i]

        ans = []

        for l, r in queries:
            if l < r:
                ans.append(prefRight[r] - prefRight[l])
            else:
                ans.append(prefLeft[l] - prefLeft[r])

        return ans

# For every index, find closest adjacent index based on smaller difference.
# Moving to closest index costs 1, otherwise cost is absolute difference.
# Precompute movement cost from left to right and right to left.
# Use prefix sums to answer each query in O(1).