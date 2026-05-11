class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        firstColZero = False

        for r in range(ROWS):
            if matrix[r][0] == 0:
                firstColZero = True

            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for c in range(COLS):
                matrix[0][c] = 0
        
        if firstColZero == True:
            for r in range(ROWS):
                matrix[r][0] = 0
