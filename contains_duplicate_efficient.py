"""
Problem: Contains Duplicate
Description: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Approach: Efficient (Hash Set)
Sets in Python are implemented as hash tables and do not allow duplicate values.
We can either iterate and add to a set, checking if the item exists, or just compare the length of the array to the length of a set created from the array.
"""

def contains_duplicate_efficient(nums):
    # Initialize an empty set to keep track of seen numbers
    seen = set()
    
    # Iterate through the numbers in the array
    for num in nums:
        # Check if the number is already in the set
        if num in seen:
            # We found a duplicate!
            return True
        # Add the number to the set for future checks
        seen.add(num)
        
    # No duplicates found
    return False

# Alternative 1-liner approach:
# def contains_duplicate_efficient_oneliner(nums):
#     return len(set(nums)) != len(nums)

# Complexity Analysis:
# Time Complexity: O(n) as we traverse the array once and set lookups/insertions are O(1) on average.
# Space Complexity: O(n) to store the numbers in the set. In worst case, all numbers are unique.
