# Problem: Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:  
        left, right = 0, 1 # left=buy, right=sell   
        maxProfit = 0   # Keep track of the max profit

        while right < len(prices):  # While the right pointer is less than the length of the array
            if prices[left] < prices[right]:    # If the left pointer is less than the right pointer
                profit = prices[right] - prices[left]   # Calculate the profit
                maxProfit = max(maxProfit, profit)  # Update the max profit
            else:   # If the left pointer is greater than the right pointer
                left = right    # Move the left pointer to the right pointer
            right += 1  # Increment the right pointer
        
        return maxProfit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))