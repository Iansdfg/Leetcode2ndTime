class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0]==1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0 for i in range(n+1)]for i in range(m+1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i - 1][j - 1] == 1:
                    dp[i][j] = 0
                else:
                    if i == j == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        print(dp)
        return dp[m][n]






