#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        # your code here
        res = [0, 1]
        if n ==1 or n==2:
            return res[:n]
        for i in range(2, n):
            res.append(res[i-1]+res[i-2])
        return res