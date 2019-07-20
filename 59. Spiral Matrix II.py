class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        direction = 0 
        top,bottom,left,right = 0,n-1,0,n-1
        curr = 1
        while True:
            for i in range(left, right+1):
                res[top][i]=curr
                curr+=1
            top+=1

            for i in range(top, bottom+1):
                res[i][right]=curr
                curr+=1
            right-=1

            for i in range(right, left-1,-1):
                res[bottom][i]=curr
                curr+=1
            bottom-=1

            for i in range(bottom, top-1,-1):
                res[i][left]=curr
                curr+=1
            left+=1

            if left>right or top>bottom: return res
    
            dirction = (direction+1)%4
        
