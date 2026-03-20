"""
Problem: Valid Anagram
Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Approach: Normal (Sorting)
Since anagrams must contain exactly the same characters with the same frequencies, sorting both strings will produce identical strings if they are anagrams.
"""

def is_anagram_normal(s, t):
    # If lengths are different, they can't be anagrams
    if len(s) != len(t):
        return False
        
    # Convert strings to sorted lists of characters
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    
    # Compare the sorted lists
    # If they are exactly the same, then 't' is an anagram of 's'
    return sorted_s == sorted_t

# Complexity Analysis:
# Time Complexity: O(n log n) where n is the length of the strings. The sorting operation takes O(n log n) time.
# Space Complexity: O(n) because sorted() creates a new list (strings are immutable in Python).
