class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m,n = len(grid),len(grid[0])
        dp =[[0 for _ in range(n+1)]for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1:
                    dp[i][j] = grid[i-1][j-1] + dp[i][j-1]
                elif j == 1:
                    dp[i][j] = grid[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j]=min(grid[i-1][j-1]+dp[i-1][j], grid[i-1][j-1]+dp[i][j-1])
        return dp[m][n]
        
