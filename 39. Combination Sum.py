class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.findSum(candidates, target, [],res)
        return res
    
    def findSum(self, candidates, target, path,res):
        if sum(path)>target:
            return 
        if sum(path)==target:
            res.append(path)
            return 
        for i in xrange(len(candidates)):
            self.findSum(candidates[i:], target, path+[candidates[i]],res)
        
        
