class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []

        # Initialize boundaries
        top, bottom, left, right = 0, m - 1, 0, n - 1

        # Iterate until all elements are printed
        while top <= bottom and left <= right:

            # Print top row from left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # Print right column from top to bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # Print bottom row from right to left (if exists)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

                # Print left column from bottom to top (if exists)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res

        # Time Complexity: O(m*n)
        # Auxiliary Space: O(1).