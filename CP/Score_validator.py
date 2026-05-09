"""
Problem: Score Validator
Platform: LeetCode
Link: 
Approach: Simulation / Counting
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def scoreValidator(self, events):
        """
        :type events: List[str]
        :rtype: List[int]
        """

        c = 0
        s = 0

        for e in events:

            if c == 10:
                break

            if e in ["0", "1", "2", "3", "4", "6"]:
                s += int(e)

            elif e == "W":
                c += 1

            elif e == "WD" or e == "NB":
                s += 1

        return [s, c]


# Traverse all events and simulate score calculation.
# Numeric events directly add runs to total score.
# 'W' increases wicket count.
# 'WD' and 'NB' contribute one extra run.
# Stop processing once 10 wickets are lost.