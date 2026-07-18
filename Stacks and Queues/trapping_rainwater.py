class Solution:
    def maxWater(self, arr):
        # code here
        n = len(arr)
        st = []
        water = 0

        for i in range(n):
            while st and arr[i] > arr[st[-1]]:
                bottom = st.pop()

                if not st:
                    break

                left = st[-1]

                width = i - left - 1
                height = min(arr[left], arr[i]) - arr[bottom]

                water += width * height

            st.append(i)

        return water