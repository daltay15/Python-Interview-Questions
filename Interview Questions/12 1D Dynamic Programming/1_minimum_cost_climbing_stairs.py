 # You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.

# Example 1:
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.

# Example 2:
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].

class Solution:
    def minCostClimbingStairs(self, cost): 
        cost.append(0) # Add 0 to the end of the list
        for i in range(len(cost) -3, -1, -1): # Start from the third last step
            cost[i] += min(cost[i + 1], cost[i + 2]) # Add the minimum cost of the next step or the next next step to the current step

        return min(cost[0], cost[1]) # Return the minimum cost of the first step or the second step
    
if __name__ == '__main__':
    cost = [10, 15, 20]
    solution = Solution()
    print(solution.minCostClimbingStairs(cost))