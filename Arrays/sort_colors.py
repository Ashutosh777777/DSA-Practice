class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red = nums.count(0)
        white = nums.count(1) + red
        blue = nums.count(2) + white

        i = 0
        while i < blue:
            if i < red:
                nums[i] = 0
                i+=1
                continue
            if i < white:
                nums[i] = 1
                i+=1
                continue
            if i < blue:
                nums[i] = 2
                i+=1
                continue
        return nums