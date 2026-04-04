"""
Problem: Remove Duplicates from Sorted List
Platform: LeetCode
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Approach: Two pointers (in-place traversal)
Time Complexity: O(n)
Space Complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        if not head.next:
            return head
        p1 = head
        p2= head.next

        while p2:
            if p1.val==p2.val:
                p1.next = p2.next
                p2 = p2.next
            else:
                p1 = p1.next
                p2 = p2.next
        return head
# Use two pointers p1 (current unique node) and p2 (next node) to traverse the list.
# If values match, skip the duplicate by linking p1.next to p2.next.
# If values differ, move both pointers forward normally.
# Continue until the end, modifying the list in-place to remove duplicates.