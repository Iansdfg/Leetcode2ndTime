# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        self.preOder(root, res)
        return res == sorted(res) and len(set(res)) == len(res)
    
    
    def preOder(self, root, res):
        if root:
            self.preOder(root.left, res)
            res.append(root.val)
            self.preOder(root.right, res)
            
        
