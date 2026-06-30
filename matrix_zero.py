class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        a = len(matrix)
        b = len(matrix[0])

        # while testing i realsized that i am not going to get right answer if matrix[0][0] is 0
        
        row_one_0 = 0
        col_one_0 = 0
        for j in range(b):
            if matrix[0][j] == 0:
                row_one_0 = 1
        
        for i in range(a):
            if matrix[i][0] == 0:
                col_one_0 = 1
        

        # i wanted to make it O(1)space complexity so i tried to use matrix itself to track which rows and columns should have 0
        # instead of using seperate lists to track which rows and col should have 0

        # find row, col containing a zero
        for i in range(1,a): 
            for j in range(1, b):
                if matrix[i][j] == 0:
                    # makes the first element of that row 0
                    matrix[i][0] = 0
                    # makes the first element of that col 0
                    matrix[0][j] = 0

        # set the rows and columns to zero
        for i in range(1,a):
            for j in range(1, b):
                # if first element of that row or col is a 0 that indicates that that all others elements there should also be 0's
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # update the first whole row and col to 0 
        if row_one_0 == 1:
            for j in range(b):
                matrix[0][j] = 0

        if col_one_0 == 1:
            for i in range(a):
                matrix[i][0] = 0


"""
i got O(m*n) time and O(m+n) space complexity for this old solution on leetcode

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
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
"""