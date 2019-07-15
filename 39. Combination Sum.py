class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, res, [])
        return res
    
    def dfs(self, candidates, target, depth, res, path):
        if target<0:
            return 
        if target==0:
            res.append(path)
            return 
        for i in range(depth, len(candidates)):
            if candidates[depth]>target:
                return 
            self.dfs(candidates, target-candidates[i], i, res, path+[candidates[i]])
