"""
Problem: Two Sum
Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Approach: Normal (Brute Force)
We check every possible pair of numbers in the array to see if their sum equals the target.
"""

def two_sum_normal(nums, target):
    n = len(nums)
    # Loop through each element 'i'
    for i in range(n):
        # Loop through the rest of the elements 'j' after 'i'
        for j in range(i + 1, n):
            # Check if the sum of the element at 'i' and 'j' equals the target
            if nums[i] + nums[j] == target:
                return [i, j] # Return their indices
    
    return [] # Return empty list if no such pair exists (though problem guarantees one solution)

# Complexity Analysis:
# Time Complexity: O(n^2) where n is the number of elements in nums. We iterate over the array in a nested loop.
# Space Complexity: O(1) as we don't use any extra space that scales with input size.
