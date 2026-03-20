"""
Problem: Two Sum
Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Approach: Efficient (Using Hash Map)
We use a dictionary to store the numbers we have seen so far and their indices.
For each number, we calculate its complement (target - number) and check if it exists in the dictionary.
"""

def two_sum_efficient(nums, target):
    # Dictionary to store the number and its index: {number: index}
    seen = {}
    
    # Iterate through the array using enumerate to get both index and value
    for current_index, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # If complement is already in our dictionary, we found the pair!
        if complement in seen:
            return [seen[complement], current_index]
        
        # Otherwise, add the current number and its index to the dictionary
        seen[num] = current_index
        
    return []

# Complexity Analysis:
# Time Complexity: O(n) because we traverse the list containing n elements exactly once. Dictionary lookups take O(1) time on average.
# Space Complexity: O(n) to store at most n elements in the hash map.
