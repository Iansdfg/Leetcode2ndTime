class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        return self.findTree(1, n)
    
    def findTree(self,left, right):
        if left > right:
            return [None]
        res = []
        for i in range(left, right+1):
            left_nodes = self.findTree(left, i-1)
            right_nodes = self.findTree(i+1, right)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)
        return res
