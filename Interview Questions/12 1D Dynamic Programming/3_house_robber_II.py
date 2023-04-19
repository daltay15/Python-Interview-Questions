# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed. All houses at this
# place are arranged in a circle. That means the first house is the
# neighbor of the last one. Meanwhile, adjacent houses have security
# system connected and it will automatically contact the police if two
# adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money
# of each house, determine the maximum amount of money you can rob
# tonight without alerting the police.

# Example 1:
# Input: nums = [2, 3, 2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.

# Example 2:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

class Solution:
    def rob(self, nums):
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1])) # Return the maximum value of the first house only or not robbing the first house or not robbing the last house

    
    def helper(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            newRob = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
    
if __name__ == '__main__':
    nums = [1,2,3,1]
    solution = Solution()
    print(solution.rob(nums))