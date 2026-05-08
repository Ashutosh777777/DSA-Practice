class Solution:
    def removeDuplicates(self, arr):
        # code here 
        res = []
        for num in arr:
            if len(res)==0 or res[-1]!=num:
                res.append(num)
        return res