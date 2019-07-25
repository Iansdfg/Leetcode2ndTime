class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        first_col_has_zero = False
        R,C = len(matrix),len(matrix[0])
        for i in range(R):
            if matrix[i][0] == 0:
                    first_col_has_zero = True
            for j in range(1,C):
                if matrix[i][j] == 0:
                    matrix[0][j]=0
                    matrix[i][0]=0
                    
        for i in range(1,R):
            for j in range(1,C):
                if not matrix[0][j] or not matrix[i][0]:
                    matrix[i][j] = 0
                    
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0
        if first_col_has_zero:
            for i in range(R):
                matrix[i][0] = 0
            
