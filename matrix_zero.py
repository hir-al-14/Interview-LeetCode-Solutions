class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
       """
        Do not return anything, modify matrix in-place instead.
        """
        a = len(matrix)
        b = len(matrix[0])

        rows_with_0 = [0] * a
        cols_with_0 = [0] * b

        # find row, col containing a zero
        for i in range(a):
            for j in range(b):
                if matrix[i][j] == 0:
                    rows_with_0[i] = 1
                    cols_with_0[j] = 1

        for i in range(a):
            for j in range(b):
                if rows_with_0[i] or cols_with_0[j]:
                    matrix[i][j] = 0
             