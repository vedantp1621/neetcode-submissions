class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # for each cell, attempt to start the matching word (only will start if the first char matches)  
        # use dfs with (row, col, i) -> i is the index in word we need to match
        # in dfs: 
        #   if i == len(word), end case we return true
        #   if out of bounds, error, mismatch, return false
        #   mark that row, col pair as visited
        #   recurse to 4 neighbors with i+1 
        #   now go back and unmark that (row, col)  
        #

        ROWS, COLS = len(board), len(board[0])
        path = set() # these are the visited chars within this context window

        def dfs(row, col, i):
            if i == len(word):
                return True # end case where we return true

            # this is the part that is likely not in an interview:
            if (min(row, col) < 0 or
                row >= ROWS or col >= COLS or
                word[i] != board[row][col] or
                (row, col) in path):
                return False

            path.add((row, col))
            res = (dfs(row+1, col, i+1) or
                   dfs(row, col+1, i+1) or
                   dfs(row-1, col, i+1) or
                   dfs(row, col-1, i+1))
            path.remove((row, col)) # backtracking step
            return res
            # end

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
                        
        return False


    

            