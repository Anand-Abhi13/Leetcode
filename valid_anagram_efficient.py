"""
Problem: Valid Anagram
Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Approach: Efficient (Hash Map / Frequency Counter)
We count the occurrences of each character in both strings. If the counts match perfectly, they are anagrams.
We can use an array of size 26 (if only lowercase English letters) or a hash map.
"""

def is_anagram_efficient(s, t):
    # If lengths differ, it's impossible to be anagrams
    if len(s) != len(t):
        return False
        
    # Dictionary to keep track of character frequencies
    count = {}
    
    # Iterate through both strings simultaneously
    # We increase the count for characters in 's' and decrease for characters in 't'
    for i in range(len(s)):
        # Process character from s
        count[s[i]] = count.get(s[i], 0) + 1
        
        # Process character from t
        count[t[i]] = count.get(t[i], 0) - 1
        
    # Check if all frequencies returned to 0
    # If any count is not 0, it means the strings had different character frequencies
    for val in count.values():
        if val != 0:
            return False
            
    return True

# Complexity Analysis:
# Time Complexity: O(n) where n is the length of the string. We iterate over the strings once.
# Space Complexity: O(1) mostly since the dictionary will have at most 26 keys (for English lowercase letters). Thus it's O(1) or O(k) where k is the character set.
