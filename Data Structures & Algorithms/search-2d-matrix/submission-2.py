class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we're dealing with 2D arrays here, so we need two #s for each index
        # i initially opted to use tuples for this, but tuples are immutable, so it wouldnt
        # work. Instead, we're going to use simple grid math to track indexes with 
        # single digit #s (for example a 4x4 grid would be numbered 0-15), and then convert
        # these single dig #s to indexes
        # Row: index# // # columns
        # Col: index# // # columns

        ROWS, COLS = len(matrix), len(matrix[0]) # init # of rows and columns as static vars
        l, r = 0, ROWS * COLS - 1 # start left as 0 right as # of items-1
        while l <= r: # simple binary search looping strategy. review pg. 15 for a reminder
            m = l + (r - l) // 2 # integer division to ensure all #s dont become decimals
            row, col = m // COLS, m % COLS # heres the conversion mentioned above
            if target > matrix[row][col]: # left gets to be pushed one beyond, since we 
                                          # are checking that it is bigger than middle
                l = m + 1
            elif target < matrix[row][col]: # right gets set to middle -1 since we already
                                            # checked to ensure it is less than middle
                r = m - 1
            else:
                return True # if this is triggered, that means target is neither > than
                            # or < than middle, which means it is the middle
        return False