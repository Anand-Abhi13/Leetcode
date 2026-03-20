"""
Problem: Contains Duplicate
Description: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Approach: Normal (Sorting)
First, we sort the array. If there are duplicates, they will be adjacent to each other after sorting.
We can then just iterate through the sorted array and check if any adjacent elements are equal.
"""

def contains_duplicate_normal(nums):
    # Sort the array first
    # Sorting takes time, but makes finding duplicates easier
    nums.sort()
    
    n = len(nums)
    # Iterate through the array up to the second to last element
    for i in range(n - 1):
        # Compare the current element with the next element
        if nums[i] == nums[i + 1]:
            # If they are the same, we found a duplicate!
            return True
            
    # If we loop through without finding any matching adjacent elements, all elements are unique
    return False

# Complexity Analysis:
# Time Complexity: O(n log n) because sorting the array takes O(n log n) time, and the explicit loop takes O(n) time.
# Space Complexity: O(1) or O(n) depending on the sorting algorithm used by Python (Timsort uses O(n) space).
