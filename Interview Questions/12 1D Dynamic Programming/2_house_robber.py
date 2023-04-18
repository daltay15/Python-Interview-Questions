# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and 
# it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
# money you can rob tonight without alerting the police.

# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.


class Solution:
    def rob(self, nums):
        rob1, rob2 = 0, 0 # rob1 is the value of the previous step, rob2 is the value of the previous previous step
        for num in nums:
            temp = max(num + rob1, rob2) # temp is used to store the value of rob1 for setting the value of rob2
            rob1 = rob2 # rob1 is the value of rob2
            rob2 = temp

        return rob2
    
if __name__ == '__main__':
    nums = [2,7,9,3,1]
    solution = Solution()
    print(solution.rob(nums))