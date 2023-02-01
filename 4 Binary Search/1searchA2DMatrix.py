# Problem: Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Given an m x n matrix and a target value, return true if the target value exists in the matrix, otherwise return false.

# Approach: Use binary search to find the row and then use binary search to find the column
# Time Complexity: O(log(m) + log(n)) = O(log(mn))
# Space Complexity: O(1)

List = list # For type hinting


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])    # Get the number of rows and columns

        top, bottom = 0, ROWS - 1   # Top and bottom pointers

        while top <= bottom:    # While the top pointer is less than or equal to the bottom pointer
            row = (top + bottom) // 2   # Get the midpoint of the row
            if target > matrix[row][-1]:    # If the target is greater than the last element in the row
                top = row + 1   # Move the top pointer down 1
            elif target < matrix[row][0]:   # If the target is less than the first element in the row
                bottom = row - 1    # Move the bottom pointer up 1
            else:   # Found the row
                break   # Break out of the loop
        
        if not (top <= bottom):    # If the top pointer is greater than the bottom pointer, return false
            return False    # If the top pointer is greater than the bottom pointer, return false
        row = (top + bottom) // 2   # Get the midpoint of the row
        l, r = 0, COLS - 1  # Left and right pointers
        while l <= r:   # While the left pointer is less than or equal to the right pointer
            m = (l + r) // 2    # Get the midpoint of the column
            if target > matrix[row][m]: # If the target is greater than the midpoint
                l = m + 1   # Move the left pointer right 1
            elif target < matrix[row][m]:   # If the target is less than the midpoint
                r = m - 1   # Move the right pointer left 1
            else: return True   # Found the target
        return False    # Not found

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(Solution().searchMatrix(matrix, target))