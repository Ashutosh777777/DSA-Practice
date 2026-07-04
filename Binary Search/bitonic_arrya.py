class Solution:

	def findMaximum(self, arr):
		# code here
# 		n = len(arr)
# 		if n == 1:
# 		    return arr[0]
# 		if arr[-1]>arr[-2]:
# 		    return arr[-1]
# 		s = 0
# 		e = n-1
		
# 		while s<= e:
# 		    m = (s+e)//2
# 		    if (m<e and arr[m-1]<arr[m]) and (m>s and arr[m+1] < arr[m]):
# 		        return arr[m]
# 	        elif arr[s] < arr[m]:
# 	            s = m+1
#             else:
#                 e = m-1
        s = 0
        e = len(arr) - 1

        while s < e:
            m = (s + e) // 2

            if arr[m] < arr[m + 1]:
                s = m + 1
            else:
                e = m

        return arr[s]