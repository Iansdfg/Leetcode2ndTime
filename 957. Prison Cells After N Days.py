class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        N%=14
        if N == 0:
            N = 14
        while N:
            newcells = [0] * 8
            for i in range(1, len(cells)-1):
                if cells[i-1]==cells[i+1]:
                    newcells[i]=1
                else:
                    newcells[i]=0
            cells = newcells
            N-=1
        return cells
                
        
