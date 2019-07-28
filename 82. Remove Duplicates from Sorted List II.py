# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: 
    def deleteDuplicates(self, head):
        prev = dummy = ListNode(-1)
        curr = dummy.next = head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if prev.next is curr:
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
        return dummy.next
                
