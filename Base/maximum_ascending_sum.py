class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        i = 0
        j = 1
        s = nums[0]
        if len(nums)==1:
            return nums[0]
        if not nums:
            return 0
        while j<len(nums):
            if nums[j]<=nums[j-1]:
                i = j
                                
            s = max(s, sum(nums[i:j+1]))
            j+=1
        return s