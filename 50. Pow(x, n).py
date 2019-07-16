class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = 1
        sign = 1 if n>0 else -1
        n = abs(n)
        while n:
            if n%2: ans*=x
            n//=2
            x*=x
            print(ans,n,x)
        if sign<0:
            ans = 1/ans
        return ans
