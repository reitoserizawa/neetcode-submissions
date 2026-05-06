class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowest, highest = matrix[0][0], matrix[-1][-1]

        if target < lowest or target > highest:
            return False

        top, bottom = 0, len(matrix)-1

        while top <= bottom:
            mid = (top + bottom) // 2
            if target > matrix[mid][-1]:
                top += 1
            elif target < matrix[mid][0]:
                bottom -= 1
            else:
                break
        
        if not top <= bottom:
            return False
        
        m = (top+bottom)//2
        l, r = 0, len(matrix[0])-1

        while l <= r:
            mid = (l+r)//2
            if target < matrix[m][mid]:
                r = mid-1
            elif matrix[m][mid] < target :
                l = mid+1
            elif matrix[m][mid] == target:
                return True
        
        return False