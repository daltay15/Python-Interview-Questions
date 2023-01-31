# Problem: Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Given an m x n matrix and a target value, return true if the target value exists in the matrix, otherwise return false.

# Approach: Use binary search to find the row and then use binary search to find the column
# Time Complexity: O(log(m) + log(n)) = O(log(mn))
# Space Complexity: O(1)

List = list
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])\

        top, bottom = 0, ROWS - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        
        if not (top <= bottom):
            return False
        row = (top + bottom) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else: return True
        return False

if __name__ == "__main__":
    print(Solution().searchMatrix(matrix, target))