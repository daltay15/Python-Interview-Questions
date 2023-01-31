# Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


List = list
nums = [2,7,11,15]
target = 9


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum(nums, target))