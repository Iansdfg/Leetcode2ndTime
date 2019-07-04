class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        N = len(board)
        def get(s):
            quot,rem = divmod(s-1, N)
            row = N-1-quot
            col = rem if N%2 != row%2 else N-1-rem
            return row,col   
            
        dist = {1:0}
        queue = collections.deque([1])
        while queue:
            s = queue.popleft()
            if s == N*N: return dist[s]
            for steps in range(s+1, min(s+6, N*N)+1):
                r, c = get(steps)
                if board[r][c]!=-1:
                    steps = board[r][c]
                if steps not in dist:
                    dist[steps] = dist[s]+1
                    queue.append(steps)
        return -1
        
        
