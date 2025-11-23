# LeetCode 1: Two Sum
# Concept: Dictionary (Hash Map) for O(n) speed

def twoSum(nums, target):
    """
    Finds the indices of two numbers that add up to target.
    """
    # Key: The number we need, Value: The index of the number we have
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    return []

# Test
print(twoSum([2,7,11,15], 9)) # Expected: [0, 1]
