# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small_curr = small = ListNode(-1)
        large_curr = large = ListNode(-1)
        while head:
            if head.val>=x:
                large_curr.next = ListNode(head.val)
                large_curr = large_curr.next
            else:
                small_curr.next = ListNode(head.val)
                small_curr = small_curr.next
            head = head.next
        small_curr.next = large.next
        return small.next
        
