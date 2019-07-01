"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        copy = dict()
        curr = head
        copy_curr = copy_head = Node(-1,None,None)
        while curr: 
            copy_curr.next = Node(curr.val,None,None)
            copy[curr] = copy_curr.next
            curr = curr.next
            copy_curr = copy_curr.next
        curr = head
        while curr: 
            if curr.next:
                copy[curr].next = copy[curr.next]
            if curr.random:
                copy[curr].random = copy[curr.random]
            curr = curr.next
        return copy_head.next
        
            
