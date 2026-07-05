class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) # holds sets of all seen nums within a given col
        rows = defaultdict(set) # holds sets of all seen nums within a given row
        squares = defaultdict(set)

        
        for r in range(9): # row by ro   
            for c in range(9): # col by col
                
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        return True





        