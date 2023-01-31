# Problem: Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

List = list
nums = [1,2,3,1]


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

if __name__ == '__main__':

    s = Solution()
    print(s.containsDuplicate(nums))