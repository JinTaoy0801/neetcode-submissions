class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        big = 0

        def dfs(row:int, col:int):
            if grid[row][col] == 0:
                return 0
            
            area = 1
            direction = [[1,0],[0,1],[-1,0],[0,-1]]
            grid[row][col] = 0
            for x, y in direction:
                nr = row +x
                nc = col +y
                if 0<= nr < len(grid) and 0<= nc < len(grid[0]) and grid[nr][nc] == 1:
                    area+=dfs(nr,nc)
                    
            return area
            



        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    p = dfs(row,col)
                    big = max(big, p)
                    
        return big