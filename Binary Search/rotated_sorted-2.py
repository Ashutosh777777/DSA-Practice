class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        s = 0
        n = len(nums)
        e = n -1 

        while s<=e:
            m = (s+e)//2
            if nums[m] == target:
                return True
            if nums[s]==nums[m]==nums[e]:
                s+=1
                e-=1
                continue
            if nums[s]<= nums[m]:
                if nums[s]<= target < nums[m]:
                    e = m-1
                else:
                    s = m + 1
            else:
                if nums[m]<=nums[e]:
                    if nums[m]< target <= nums[e]:
                        s = m + 1
                    else:
                        e = m-1
        return False
