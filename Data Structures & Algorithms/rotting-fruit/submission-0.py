from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        minute = 0
        fresh = 0
        #find rotting fruit
        q = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh+=1
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                rf = q.popleft()
                for dr, dc in directions:
                    row, col = rf[0] + dr, rf[1] + dc
                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                        q.append((row,col))
                        grid[row][col] = 2
                        fresh-=1
            minute += 1
            
        return minute if fresh == 0 else -1