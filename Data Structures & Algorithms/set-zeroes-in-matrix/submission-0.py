class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        spareMatrix = [[0] * (COLS+1) for _ in range(ROWS+1)]

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    spareMatrix[0][c+1] = 1
                    spareMatrix[r+1][0] = 1
        
        for r in range(ROWS+1):
            if spareMatrix[r][0] == 1:
                for c in range(COLS):
                    matrix[r-1][c] = 0
        
        for c in range(COLS+1):
            if spareMatrix[0][c] == 1:
                for r in range(ROWS):
                    matrix[r][c-1] = 0
        



