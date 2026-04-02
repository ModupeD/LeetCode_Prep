# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# Example 1:
# Input: nums = [1, 2, 3, 3]
# Output: true

# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hash_map = Counter(nums)
        for key,value in nums_hash_map.items():
            if value > 1:
                return True
        return False
# TC: O(N)
# SC: O(N)

# counter is O(N)