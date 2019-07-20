class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        nums = [1,2,3,4,5,6,7,8,9]
        frac = 1
        k-=1
        for i in xrange(1,n):
            frac*= i
        for i in xrange(n-1,-1,-1):
            curr = nums[k//frac]
            res+= str(curr)
            nums.remove(curr)
            if i>0:
                k%=frac
                frac//=i
        return res
