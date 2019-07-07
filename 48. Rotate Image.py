# class Solution(object):
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """
#         n = len(matrix)
#         for x in xrange(n):
#             for y in xrange(n):
#                 if x<y:
#                     matrix[x][y],matrix[y][x]= matrix[y][x],matrix[x][y]
#         for row in matrix:
#             row.reverse()
            
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in range(n//2):
            first = layer
            last = n-1-layer
            for i in range(first,last):
                offset = i-first
                top = matrix[first][i]
                matrix[first][i] = matrix[last-offset][first]
                matrix[last-offset][first] = matrix[last][last-offset]
                matrix[last][last-offset] = matrix[i][last]
                matrix[i][last] = top

                
