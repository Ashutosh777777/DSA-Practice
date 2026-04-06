"""
Problem: Remove Nth Node From End of List
Platform: LeetCode
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Approach: Two-pass (count length, then delete node)
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count = 0
        cur = head
        
        # count length
        while cur:
            cur = cur.next
            count += 1
        
        # remove head case
        if n == count:
            return head.next
        
        cur2 = head
        for _ in range(count - n - 1):
            cur2 = cur2.next
        
        cur2.next = cur2.next.next
        
        return head
# Traverse the list once to calculate its total length.
# Compute the position of the node to delete: (length − n).
# Traverse again to the node just before the target node.
# Adjust pointers to skip the target node and remove it.