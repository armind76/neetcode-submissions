class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rowlen = len(grid)
        collen = len(grid[0])
        res = 0
        def dfs(row,col):
            if row < 0 or col < 0 or row >= rowlen or col >= collen or grid[row][col] == "0" :
                return 
            

            grid[row][col] = "0"
            dfs(row + 1 , col)
            dfs(row - 1 , col)
            dfs(row, col + 1)
            dfs(row, col - 1)
                 
        for i,row in enumerate(grid):
            for j,node in enumerate(row):
                if node == "1":
                    res += 1
                    dfs(i,j)
        return res
