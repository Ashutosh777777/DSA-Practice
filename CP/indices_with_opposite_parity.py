"""
Problem: Count Indices With Opposite Parity
Platform: LeetCode Weekly Contest 500
Link: https://leetcode.com/contest/weekly-contest-500/problems/count-indices-with-opposite-parity/
Approach: Suffix Count of Even/Odd Numbers
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def countOppositeParity(self, nums):
        n = len(nums)
        ans = [0] * n
        even = 0
        odd = 0

        for i in range(n - 1, -1, -1):
            if nums[i] % 2 == 0:
                even += 1
                ans[i] = odd
            else:
                odd += 1
                ans[i] = even

        return ans

# Traverse from right to left.
# Maintain count of even and odd numbers after current index.
# If nums[i] is even, answer is count of odd numbers after it.
# If nums[i] is odd, answer is count of even numbers after it.