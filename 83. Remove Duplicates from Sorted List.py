# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead = dummy = ListNode(-1)
        dic=[]
        while head:
            if head.val not in dic:
                dic.append(head.val)
                dummy.next = ListNode(head.val)
                dummy = dummy.next
            head = head.next
        return newhead.next
                
        
        
