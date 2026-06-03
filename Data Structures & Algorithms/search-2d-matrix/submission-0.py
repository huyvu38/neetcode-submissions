class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col - 1
        while left <= right:
            mid = (left + right) // 2
            #row_index assume how many full rows of size have pass
            row_index = mid // col
            #col_index is like remainder
            col_index =mid % col
            if matrix[row_index][col_index] == target:
                return True
            elif matrix[row_index][col_index ] > target:
                right = mid -1
            else:
                left = mid+1
        return False

