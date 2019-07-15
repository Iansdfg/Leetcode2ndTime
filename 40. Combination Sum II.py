class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.findSum(candidates, target, 0, [], res)
        return res
    
    def findSum(self, candidates, target, depth, path, res):
        if target<0:
            return
        if target == 0:
            res.append(path)
            return
        for i in range(depth,len(candidates)):
            if candidates[depth]>target:
                return 
            curr = candidates[i]
            if i > depth and candidates[i] == candidates[i-1]:
                continue
            self.findSum(candidates, target-curr, i+1, path+[curr], res)
        
