class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        sign = 1 if n>0 else -1
        res, n = 1, abs(n)
        while n:
            if n%2:res*=x
            x*=x
            n//=2

        return res if sign>0 else 1/res
        
