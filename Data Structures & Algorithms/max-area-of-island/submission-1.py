class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        ts is identical to the one before it so lets see if we can figure it out

        bfs or dfs idk if it makes a real difference 
        bfs cuz ik it
        size = 0
        bfs(r,c):
            base case r > rows or c > cols and more than 0 for both or node == 0:
                return 0
            grid[r] [c] = 0
            return 1 + bfs(size,r+1,c) + .... 
        loop:
        if 1:
            size = max(size,dfs(r,c))
        eles nothing
        '''
        if not grid:
            return 0
        res = 0
        ROWS,COLS = len(grid),len(grid[0])
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c>= COLS  or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r, c+1) + dfs(r,c-1)
        
        for i, row in enumerate(grid):
            for j, col in enumerate(grid[i]):
                if col == 1: #idk if its a string or int
                    size = dfs(i,j)
                    res = max(size,res)
        return res