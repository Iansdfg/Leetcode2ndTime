class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [1]+[0]*(len(s))
        for i in range(1,len(dp)):
            if s[i-1]!='0': 
                dp[i]+=dp[i-1]
            if i>1 and '10'<= s[i-2:i]<='26':
                dp[i]+=dp[i-2]
        return dp[-1]
                
            
        
