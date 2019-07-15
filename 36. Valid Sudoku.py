class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidSqr(board)
        
    def isValidRow(self, board):
        for r in range(len(board)):
            row = [ ele for ele in board[r] if ele != '.' ]
            if len(row) != len(set(row)):
                return False
        return True
            
        
    def isValidCol(self, board):
        for c in range(len(board)):
            col = [board[r][c] for r in range(len(board)) if board[r][c] != '.']
            if len(col) != len(set(col)):
                return False
        return True
        
        
    def isValidSqr(self, board):
        for row in range(0,len(board),3):
            for col in range(0,len(board),3):
                sqr = []
                for i in range(3):
                    for j in range(3):
                        ele = board[row+i][col+j]
                        if ele!='.':
                            sqr.append(ele)
                        if len(sqr) != len(set(sqr)):
                            return False            
        return True
        
