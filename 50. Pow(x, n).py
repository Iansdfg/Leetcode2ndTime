class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        sign = 1 if n>0 else -1
        n, ans = abs(n), 1
        while n:
            if n%2: ans*=x
            n//=2
            x*=x
        return ans if sign>0 else 1/ans
