# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        value = 0
        res = curr = ListNode(-1)
        while l1 or l2 or value:
            if l1: 
                value+=l1.val 
                l1 = l1.next
            if l2: 
                value+=l2.val 
                l2 = l2.next
            curr.next = ListNode(value%10)
            curr = curr.next
            value = value//10
        return res.next
            
        
