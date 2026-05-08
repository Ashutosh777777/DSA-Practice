#User function Template for python3

class Solution:
    def getPairs(self, arr):
        # code here
        # arr = sorted(arr)
        arr.sort()
        res = set()

        i = 0
        j = len(arr) - 1

        while i < j:
            total = arr[i] + arr[j]

            if total == 0:
                res.add((arr[i], arr[j]))
                i += 1
                j -= 1

            elif total > 0:
                j -= 1

            else:
                i += 1

        return [list(pair) for pair in sorted(res)]