# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:return head
        newhead = dummy = ListNode(-1)
        dummy.next = head
        while dummy.next and dummy.next.next:
            
            node = dummy.next
            nextt = node.next
            
            node.next = nextt.next
            nextt.next = node
            dummy.next = nextt

            dummy = dummy.next.next
        return newhead.next
 
