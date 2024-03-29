# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.symm(root,root)
        
    def symm(self, left, right):
        if not left and not right: return True
        if not left or not right: return False
        return left.val == right.val and self.symm(left.left,right.right) and self.symm(left.right,right.left)
            
                

            
        
        
