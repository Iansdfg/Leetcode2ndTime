class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.comb(n, k, 1, [],res)
        return res

    def comb(self,n, k,level, path,res):
        if len(path)==k:
            res.append(path)
            return
        for i in range(level,n+1):
            self.comb(n, k, i+1, path+[i],res)

            

        
