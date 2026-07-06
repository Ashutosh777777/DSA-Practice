class Solution:
    def findPages(self, arr, k):
        # code here
        n = len(arr)

        if k > n:
            return -1

        s = max(arr)
        e = sum(arr)
        ans = -1

        while s <= e:
            m = (s + e) // 2

            if self.possible(arr, k, m):
                ans = m
                e = m - 1
            else:
                s = m + 1

        return ans

    def possible(self, arr, k, mx):
        stu = 1
        pages = 0

        for x in arr:
            if pages + x <= mx:
                pages += x
            else:
                stu += 1
                pages = x

                if stu > k:
                    return False

        return True