# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.level(root, 0,  res)
        print(res)
        return res
    
    def level(self, root,depth, res):
        if root:
            if len(res)==depth:
                res.append([])
            res[depth].append(root.val)
            self.level(root.left, depth+1 , res)
            self.level(root.right, depth+1 , res)
        
        
