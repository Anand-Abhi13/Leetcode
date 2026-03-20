"""
Problem: Best Time to Buy and Sell Stock
Description: You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Approach: Efficient (One Pass)
We keep track of the minimum price seen so far and the maximum profit we can get.
As we iterate through the array, we update the minimum price and calculate the profit if we were to sell today.
"""

def max_profit_efficient(prices):
    # Initialize minimum price to a very large number (infinity)
    min_price = float('inf')
    # Initialize maximum profit to 0
    max_profit = 0
    
    # Iterate through the prices exactly once
    for price in prices:
        # If we find a lower price than our current minimum, update min_price
        if price < min_price:
            min_price = price
        # Otherwise, check if selling today gives a better profit than our current max_profit
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit

# Complexity Analysis:
# Time Complexity: O(n) where n is the length of the prices array. We only iterate through the array once.
# Space Complexity: O(1) as we only use two variables (min_price and max_profit).
