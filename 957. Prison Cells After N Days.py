class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        loop = self.findLoop(cells)
        N%=loop
        if N == 0:
            N = loop
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
    
    def findLoop(self, cells):
        loop = []
        while True:
            newcells = [0] * 8
            for i in range(1, len(cells)-1):
                if cells[i-1]==cells[i+1]:
                    newcells[i]=1
                else:
                    newcells[i]=0
            cells = newcells
            if cells not in loop:
                loop.append(cells)
            else:
                return len(loop)
        
