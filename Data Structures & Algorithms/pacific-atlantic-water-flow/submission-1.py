class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        # store a visited set that keeps track of the nodes we have fully processed
        pac = set()
        atl = set()
        
        def dfs(row, col, visited, prev_height):
            # some block that ends this iteration if it is out of bounds
            if ((row, col) in visited or row < 0 or col < 0 or row >= ROWS or col >= COLS or heights[row][col] < prev_height):
                return
            
            visited.add((row,col))
            # get all neighbors larger than the current node - add them to some queue
            directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            for rtransform, ctransform in directions:
                dfs(row + rtransform, col + ctransform, visited, heights[row][col])


        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # top row - pacific
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # bottom row - atlantic
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) # left col - pacific
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) # right col - atlantic

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res

















        