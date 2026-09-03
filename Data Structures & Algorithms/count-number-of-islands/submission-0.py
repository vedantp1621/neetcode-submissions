# approach in a nutshell: 
'''

    We're first scan the grid element by element. When we find a grid location with the value 1, we then call the bfs function. That function starts by clearing the 1 value from that node, adding it to a priority queue, and then iterating through that nodes neighbors one by one. We keep the directions 2d array to apply transformations on the original node, allowing us to easily calculate the indexes of all the neighboring nodes. For each neighbor, we check if it's index is out of bounds or if it is water, in which case we skip it altogether. If it is land and in bounds, we add the neighbor to the priority queue, set it's value to 0, and then check it in the future. This way, the outermost loop only has to detect the start of an island. The bfs will go through that island and clear all the 1s to 0s, meaning that the outside loop won't detect the neighbor.

'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        # BFS - will only run on each 1 in the grid
        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    # now we check if the neighbor is out of bounds, or is water
                    if (nr >= ROWS or nc >= COLS or nr < 0 or nc < 0 or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1

        return islands



        
        