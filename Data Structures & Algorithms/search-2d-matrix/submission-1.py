class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        row = -1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row = mid
                break
            elif matrix[mid][0] < target and matrix[mid][-1] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if row == -1: return False

        inner_left = 0
        inner_right = len(matrix[0]) - 1

        while inner_left <= inner_right:
            mid = (inner_left + inner_right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                inner_left = mid + 1
            else:
                inner_right = mid - 1
        
        return False