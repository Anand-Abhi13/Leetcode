"""
Problem: Maximum Subarray
Description: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Approach: Normal (Brute Force optimized to O(n^2))
We compute the sum of all possible subarrays by fixing a starting point and exploring all ending points.
We maintain the maximum sum seen so far.
"""

def max_subarray_normal(nums):
    # Initialize max_sum to negative infinity to handle arrays with all negative numbers
    max_sum = float('-inf')
    n = len(nums)
    
    # 'i' is the starting index of the subarray
    for i in range(n):
        current_sum = 0
        # 'j' is the ending index of the subarray
        for j in range(i, n):
            # Accumulate the sum from i to j
            current_sum += nums[j]
            
            # If we found a sum greater than max_sum, update max_sum
            if current_sum > max_sum:
                max_sum = current_sum
                
    return max_sum

# Complexity Analysis:
# Time Complexity: O(n^2) where n is the length of nums. We check every possible subarray segment.
# Space Complexity: O(1) as we only use variables to store sums.
