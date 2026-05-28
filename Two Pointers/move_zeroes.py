class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        nz = 0

        while z < len(nums) and nz < len(nums):
            if nums[z] != 0:
                z += 1
                continue

            if nz <= z:
                nz = z + 1
                continue

            if nums[nz] == 0:
                nz += 1
                continue

            nums[z], nums[nz] = nums[nz], nums[z]
            z += 1
            nz += 1