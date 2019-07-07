class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for x in xrange(n):
            for y in xrange(n):
                if x<y:
                    matrix[x][y],matrix[y][x]= matrix[y][x],matrix[x][y]
        for row in matrix:
            row.reverse()
