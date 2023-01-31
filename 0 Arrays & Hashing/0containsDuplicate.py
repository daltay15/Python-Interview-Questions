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