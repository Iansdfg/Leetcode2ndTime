class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        m,n = len(matrix), len(matrix[0])
        direction = 0 
        top, bottom,left,right = 0,m-1,0,n-1
        res = []
        while True:
            if direction == 0:
                for i in range(left, right+1):
                    res.append(matrix[top][i])
                top+=1
                
            if direction == 1:
                for i in range(top, bottom+1):
                    res.append(matrix[i][right])
                right-=1
            
            if direction == 2:
                for i in range(right, left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
                
            if direction == 3:
                for i in range(bottom, top-1,-1):
                    res.append(matrix[i][left])
                left+=1
            
            if left>right or top>bottom:return res
            
            direction = (direction + 1) % 4
                    
        
