class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l,r = 0, x
        while l<=r:
            m =(l+r)//2
            if m*m > x:
                r = m-1
            else:
                l = m+1
        return r
                
