# Problem: You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Greedy approach
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1): # iterate from the end of the array to the beginning of the array by -1
            if i + nums[i] >= goal: # if the current index + the value at the current index is greater than or equal to the goal
                goal = i # set the goal to the current index
        return True if goal == 0 else False # return True if the goal is 0, otherwise return False
if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(Solution().canJump(nums))