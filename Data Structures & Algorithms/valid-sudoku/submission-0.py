class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) # detects duplicates in rows (across)
        rows = defaultdict(set) # detects duplicates in cols (down)

        squares = defaultdict(set)  # key = (r//3, c//3)

        for r in range(9): # row by row (down)
            for c in range(9): # col by col (across)
                if board[r][c] == ".": # signifies empty square, we can skip
                    continue

                # this will run three checks on duplicates 
                if ( board[r][c] in rows[r] # checks horizontal duplicates
                    or board[r][c] in cols[c] # checks vertical duplicates
                    or board[r][c] in squares[(r // 3, c // 3)]): # checks duplicates in each 9 subsquares
                    return False

                # adds to respective sets and moves on
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # if we never returned false, that means no duplicates were found
        return True