class Solution:
    def calculateSpan(self, nums):
        # code here
        n = len(nums)
        res = [0]*n
        st = []
        # st2 = []
        for i in range(n):
            # count = 1
            while st and nums[i]>=nums[st[-1]]:
                st.pop()
                
            # res[i] = count
            # while st2:
            #     st.append(st2.pop())
            if st:
                res[i] = i - st[-1]
            else:
                res[i] = i+1
                
            st.append(i)
        return res