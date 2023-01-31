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
