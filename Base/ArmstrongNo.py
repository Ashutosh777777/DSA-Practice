#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here
        return (int(str(n)[0]))**3 + (int(str(n)[1]))**3 + (int(str(n)[2]))**3 == n