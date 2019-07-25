class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:return False
        l,r = 0, len(matrix)
        while l<=r:
            m = (r+l)//2
            if m >= len(matrix):return False
            print(m)
            if target in matrix[m]:
                return True
            elif target<matrix[m][0]:
                r = m-1
            elif target>matrix[m][-1]:
                l = m+1
            elif matrix[m][0]<target<matrix[m][-1]:
                return False
            
            
        
