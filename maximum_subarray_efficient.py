"""
Problem: Maximum Subarray
Description: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Approach: Efficient (Kadane's Algorithm)
We iterate through the array while maintaining the current continuous sum.
If at any point our current sum becomes negative, it's hurting our chances for a maximum sum. 
We should discard it and start a new subarray from the next element.
"""

def max_subarray_efficient(nums):
    # Initialize max_sum to the first element (could be negative)
    max_sum = nums[0]
    # current_sum tracks the sum of the subarray we are currently evaluating
    current_sum = 0
    
    # Iterate through every number in the array
    for num in nums:
        # If the continuous sum is negative, it will only drag down future calculations
        # So we reset it to 0 before adding the current number
        if current_sum < 0:
            current_sum = 0
            
        # Add the current number to our running sum
        current_sum += num
        
        # Update the overall max_sum if current_sum is larger
        if current_sum > max_sum:
            max_sum = current_sum
            
    return max_sum

# Complexity Analysis:
# Time Complexity: O(n) because we do a single pass across the array.
# Space Complexity: O(1) because we only keep track of two variables.
