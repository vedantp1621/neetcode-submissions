class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m x n 2d array of ints
        # - each row sorted in ascending order
        # - each entire row is less than next entire row
        # integer target
        
        '''
        brute force: to search using nested loop for the integer, which would require
         0(n^2) time

        goal is to get this down to O(log m + log n)

        to optimize that, we can be binary on the middle item (n-1/2) 

        and be binary on the m value

        structure:

        bs on the m value until you find something 
        bs on the n value until ypou find something
        '''
        array = [[1,2,3], [4,5,7], [7,8,9]]
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1

        while l <= r:
            m = l + (r-l) // 2

            row, col = m // COLS, m % COLS # // maps to row, % maps to col

            if target > matrix[row][col]:
                l = m+1

            elif target < matrix[row][col]:
                r = m-1
            else:
                return True
        return False


        