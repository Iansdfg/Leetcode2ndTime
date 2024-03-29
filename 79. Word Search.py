class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.findNext(i,j, board, word):return True
        return False

    def findNext(self, i,j, board, word):
        if len(word)==0: return True
        if  i<0 or j<0 or i>= len(board) or j>= len(board[0]) or board[i][j]!=word[0]:return False
        tmp = board[i][j]
        board[i][j] = "#"
        res =  self.findNext(i+1,j,board, word[1:]) or self.findNext(i-1,j,board, word[1:]) or self.findNext(i,j+1,board, word[1:]) or self.findNext(i,j-1,board, word[1:])
        board[i][j] = tmp
        return res
        
        
        
