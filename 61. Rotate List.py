# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head
        curr = fast = slow = head
        count = 0
        while curr:
            count+=1
            curr = curr.next
        k = k%count
        while k:
            fast = fast.next
            count+=1
            k-=1
        if not fast: return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = head
        newHead = slow.next
        slow.next = None
        return newHead
        
