# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        res_q, res_p = [], []
        self. inOrder(q, res_q)
        self. inOrder(p, res_p)
        print(res_q, res_p)
        return res_q == res_p
        
    def inOrder(self,root, res):
        if root:
            res.append(root.val)
            self. inOrder(root.left, res)
            self. inOrder(root.right, res)
        else:
            res.append(None)

        
        
    
        
