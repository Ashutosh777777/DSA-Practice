class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count = 0

        
        # for j in range(len(nums)-1, 0, -1):
        #     for i in range(j-1, -1, -1):
        #         if nums[i]>2*nums[j]:
        #             count+=1
        # return count

        def merge(left, right):
            if left >= right:
                return 0

            mid = (left + right) // 2

            count = merge(left, mid)
            count += merge(mid + 1, right)

            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            temp = []
            i = left
            j = mid + 1

            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= right:
                temp.append(nums[j])
                j += 1

            nums[left:right + 1] = temp

            return count

        return merge(0, len(nums) - 1)