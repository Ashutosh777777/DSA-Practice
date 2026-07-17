class Solution:
    def getMaxArea(self, arr):
        # code here
        n = len(arr)

        st = []
        res = [-1] * n

        for i in range(n):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()

            if st:
                res[i] = st[-1]
            else:
                res[i] = -1

            st.append(i)

        st = []
        res2 = [n] * n

        for i in range(n - 1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()

            if st:
                res2[i] = st[-1]
            else:
                res2[i] = n

            st.append(i)

        ans = 0
        for i in range(n):
            width = res2[i] - res[i] - 1
            ans = max(ans, width * arr[i])

        return ans