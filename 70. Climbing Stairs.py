class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1,1]+[0]*(n-1)
        for i in xrange(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]
            
