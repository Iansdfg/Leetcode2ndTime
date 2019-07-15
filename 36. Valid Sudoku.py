class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.validRow(board) and self.validCol(board) and self.validSqr(board)
        
    def validRow(self, board):
        for row in range(len(board)):
            thisRow = [x for x in board[row] if x != '.']
            if len(thisRow) != len(set(thisRow)):
                return False
        return True
    
    def validCol(self, board):
        for col in range(len(board)):
            thisCol = [board[r][col] for r in range(len(board)) if board[r][col] != '.']
            if len(set(thisCol)) != len(thisCol):
                return False
        return True
    
    def validSqr(self, board):
        n = len(board)
        for r in range(0, n, 3):
            for c in range(0, n, 3):
                cell = []
                for i in range(3):
                    for j in range(3):
                        num = board[r + i][c + j]
                        if num != '.':
                            cell.append(num)
                if len(set(cell)) != len(cell):
                    return False
        return True

        
        
    
