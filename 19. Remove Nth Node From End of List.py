# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = prev = ListNode(-1)
        prev.next = fast = head
        while n:
            fast = fast.next
            n-=1
        while fast:
            fast = fast.next
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next
