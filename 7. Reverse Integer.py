class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res,neg = 0,0
        if x<0:
            x = -x
            neg = 1
        while x:
            res = res*10 + x%10
            x = x//10
            print(res)
        if res>2**31-1: return 0 
        return res if neg == 0 else -res
            
        
