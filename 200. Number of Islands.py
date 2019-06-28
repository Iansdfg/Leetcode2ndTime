class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid ==[]  or grid[0]==[]: return 0
        count = 0
        m,n = len(grid), len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1':
                    self.zeroify(grid, x, y ,m,n)
                    print(x,y)
                    count+=1
        return count
                    
        
    def zeroify(self, grid, x,y,m,n):
        if x<0 or y < 0 or x>=m or y>=n or grid[x][y]=='0':return
        grid[x][y] = '0'
        self.zeroify(grid, x+1, y, m, n)
        self.zeroify(grid, x, y+1, m, n)
        self.zeroify(grid, x-1, y, m, n)
        self.zeroify(grid, x, y-1, m, n)
        
        
