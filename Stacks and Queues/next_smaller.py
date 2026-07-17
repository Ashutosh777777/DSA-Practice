class Solution:
	def nextSmallerEle(self, arr):
		# code here
        st = []
        res = [-1]*len(arr)
        
        for i in range(len(arr)-1, -1, -1):
            while st and st[-1]>=arr[i]:
                st.pop()
            if st:
                res[i] = st[-1]
            else:
                res[i] = -1
            st.append(arr[i])
        return res