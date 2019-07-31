class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0: return ['0']
        res = ['0','1']
        for _ in range(n-1, 0, -1):
            new_res = []
            for ele in res:
                new_res.append('0'+ele)
            for ele in reversed(res):
                new_res.append('1'+ele)
            res = new_res
        ans = []
        for ele in res:
            ans.append(int(ele,2))
        return ans
            
            
        
