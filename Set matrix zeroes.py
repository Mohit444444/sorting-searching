class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        # To store which rows and columns are
        # supposed to mark with zeroes
        rows = [False] * n
        cols = [False] * m

        # Traverse the matrix to fill rows[] and cols[]
        for i in range(n):
            for j in range(m):

            # If the cell contains zero then mark
            # its row and column as zero
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        # Set matrix elements to zero if they
        # belong to a marked row or column
        for i in range(n):
            for j in range(m):

                # Mark cell (i, j) with zero if either
                # of rows[i] or cols[j] is true
                if rows[i] or cols[j]:
                    matrix[i][j] = 0

        
        # O(n*m) Time and O(1) Space