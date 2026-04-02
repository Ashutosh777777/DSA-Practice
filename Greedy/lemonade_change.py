"""
Problem: Lemonade Change
Platform: LeetCode
Link: https://leetcode.com/problems/lemonade-change/
Approach: Greedy (simulate transactions with optimal change strategy)
Time Complexity: O(n) single pass through bills
Space Complexity: O(1) constant extra space
"""
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        galla = {"5":0, "10":0, "20":0}

        for bill in bills:
            if bill == 5:
                galla["5"]+=1
            elif bill == 10:
                if galla["5"]==0:
                    return False
                else:
                    galla["5"]-=1
                    galla["10"]+=1
            else:
                if galla["10"] > 0 and galla["5"] > 0:
                    galla["10"] -= 1
                    galla["5"] -= 1
                elif galla["5"] >= 3:
                    galla["5"] -= 3
                else:
                    return False
        return True
    
#Traverse each bill and simulate transactions while maintaining count of $5 and $10 bills.
# For $10, give one $5 as change; for $20, prioritize giving one $10 + one $5.
# If not possible, give three $5 bills; otherwise return False if change cannot be made.
# Greedy works since using larger bills first preserves smaller bills for future transactions.