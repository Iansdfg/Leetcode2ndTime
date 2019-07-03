class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]: return False
        m,n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(i, j, 0, board, word): return True
        return False

    def dfs(self,x, y , i, board, word):
        if i == len(word):
            return True
        m,n = len(board), len(board[0])
        if x>=m or y>=n or x<0 or y < 0 or board[x][y]!=word[i]:
            return False
        value = board[x][y]
        board[x][y] = "#"
        res = self.dfs(x+1, y , i+1, board, word) or self.dfs(x, y+1 , i+1, board, word) or self.dfs(x-1, y , i+1, board, word)  or self.dfs(x, y-1 , i+1, board, word) 
        board[x][y] = value
        return res
        
                    
                
        
        
