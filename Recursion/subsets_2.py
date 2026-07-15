class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        cur = []

        def solve(i):
            if i == len(nums):
                res.append(cur[:])
                return

            cur.append(nums[i])
            solve(i + 1)
            cur.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            solve(i + 1)

        solve(0)
        return res