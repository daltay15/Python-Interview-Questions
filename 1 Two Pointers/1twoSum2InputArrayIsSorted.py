# 167. Two Sum II - Input array is sorted
# Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.


List = list
numbers = [2, 7, 11, 15]
target = 9

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            
            if sum > target:
                right -= 1
            
            elif sum < target:
                left += 1

            else:
                return[left + 1, right + 1]
                

if __name__ == "__main__":
    print(Solution().twoSum(numbers, target))
