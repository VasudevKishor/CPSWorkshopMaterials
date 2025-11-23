# LeetCode 242: Valid Anagram
# Concept: Sorting vs Hash Map

def isAnagram(s, t):
    """
    Checks if t is an anagram of s.
    """
    # Method 1: Sorting (Easy to understand) - O(n log n)
    # return sorted(s) == sorted(t)

    # Method 2: Dictionary Counting (Faster) - O(n)
    if len(s) != len(t):
        return False
        
    count = {}
    
    # Count chars in s
    for char in s:
        count[char] = count.get(char, 0) + 1
        
    # Subtract chars in t
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
        
    return True

# Test
print(isAnagram("anagram", "nagaram")) # Expected: True
