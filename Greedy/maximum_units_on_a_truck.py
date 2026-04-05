"""
Problem: Maximum Units on a Truck
Platform: LeetCode
Link: https://leetcode.com/problems/maximum-units-on-a-truck/
Approach: Greedy (sort by units per box in descending order)
Time Complexity: O(n log n) due to sorting
Space Complexity: O(1)
"""
class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        res = 0
        for boxes, units in boxTypes:
            take = min(boxes, truckSize)
            res += take * units
            truckSize -= take
            
            if truckSize == 0:
                break
        
        return res
# Sort box types in descending order of units per box.
# Pick boxes greedily from the highest unit value type first.
# Take as many boxes as possible without exceeding truck capacity.
# Accumulate total units until the truck is full.