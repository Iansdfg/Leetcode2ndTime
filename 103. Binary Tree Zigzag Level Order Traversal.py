# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.levelOrder(root, 0, res)
        for pos, val in enumerate(res):
            if pos%2:
                val[:] = val[::-1]
        return res
    
    def levelOrder(self, root, level, res):
        if root:
            if level >= len(res):
                res.append([])
            res[level].append(root.val)
            self.levelOrder(root.left, level+1, res)
            self.levelOrder(root.right, level+1, res)
        
        
