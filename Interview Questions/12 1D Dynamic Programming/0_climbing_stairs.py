# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n):
        one, two = 1, 1 # one step, two steps
        for i in range(n - 1): # Using Fibonacci sequence to solve this problem
            temp = one  # temp is used to store the value of one for setting the value of two
            one = one + two # one step is the sum of one step and two steps which is how many ways to reach the top from the previous step
            two = temp # two steps is the value of one step which is how many ways to reach the top from the previous step

        return one

if __name__ == '__main__':
    n = 5
    solution = Solution()
    print(solution.climbStairs(n))