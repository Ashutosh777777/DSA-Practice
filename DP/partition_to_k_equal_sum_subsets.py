"""
Problem: Partition to K Equal Sum Subsets
Platform: LeetCode
Link: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
Approach: Backtracking with pruning
Time Complexity: O(k * 2^n) in worst case (pruned heavily in practice)
Space Complexity: O(n) recursion + used array
"""
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if sum(nums) % k:
            return False

        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)

        def backtrack(i, k, subsetSum):
            if k == 1:
                return True

            if subsetSum == target:
                return backtrack(0, k - 1, 0)

            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue

                used[j] = True
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False

                if subsetSum == 0:
                    break

            return False

        return backtrack(0, k, 0)
# Check if total sum is divisible by k; each subset must sum to target = total/k.
# Sort in descending order to place larger elements first (better pruning).
# Use backtracking to build subsets, marking elements as used.
# Once a subset reaches target, recursively form the remaining k-1 subsets.