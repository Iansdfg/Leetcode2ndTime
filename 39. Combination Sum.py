class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.findSum(candidates, target, 0, [], res)
        return res
    
    def findSum(self, candidates, target, depth, path, res):
        if target < 0:
            return 
        if target == 0:
            res.append(path)
        for i in range(depth, len(candidates)):
            curr = candidates[i]
            if candidates[depth]>target:
                return 
            self.findSum(candidates, target-curr, i, path+[curr], res)
