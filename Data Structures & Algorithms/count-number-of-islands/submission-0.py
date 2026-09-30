from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        ret = 0
        
        q = deque()
        direction = [[1,0], [0,1],[-1,0],[0,-1]]

        def dfs(row:str, col:str)-> None:
            inrow = int(row)
            incol = int(col)
            if grid[inrow][incol] == "0":
                return
            grid[inrow][incol] = '0'
            for x,y in direction:

                nr = int(row)+x
                nc = int(col)+y
                if 0 <= nr < len(grid) and 0<= nc < len(grid[0]):
                    dfs(str(nr),str(nc))
                    
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    dfs(str(row),str(col))
                    
                    ret+=1


        return ret