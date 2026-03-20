"""
Problem: Best Time to Buy and Sell Stock
Description: You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Approach: Normal (Brute Force)
For every single day (buying day), we check all subsequent days (selling days) to find the maximum possible profit.
"""

def max_profit_normal(prices):
    max_profit = 0
    n = len(prices)
    
    # i represents the day we buy the stock
    for i in range(n):
        # j represents the day we sell the stock (must be after i)
        for j in range(i + 1, n):
            # Calculate the profit if we bought on day i and sold on day j
            profit = prices[j] - prices[i]
            
            # Update max_profit if we found a better profit
            if profit > max_profit:
                max_profit = profit
                
    return max_profit

# Complexity Analysis:
# Time Complexity: O(n^2) where n is the number of days. Nested loops to check all pairs.
# Space Complexity: O(1) as we only use a few variables.
