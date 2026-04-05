"""
Problem: Candy
Platform: LeetCode
Link: https://leetcode.com/problems/candy/
Approach: Greedy (two-pass: left-to-right and right-to-left)
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        left = [1]*len(ratings)
        right = [1]*len(ratings)
        
        for i in range(1, len(ratings)):
            if ratings[i]>ratings[i-1]:
                left[i] = left[i-1]+1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i]>ratings[i+1]:
                right[i] = right[i+1]+1
        res = []
        for i in range(len(ratings)):
            res.append(max(left[i], right[i]))
        return sum(res)
# Initialize two arrays to track candies required from left and right constraints.
# Traverse left→right to ensure each child with higher rating than left neighbor gets more candies.
# Traverse right→left to ensure the same condition with right neighbor.
# Final candies = max(left[i], right[i]) for each child, summed up.