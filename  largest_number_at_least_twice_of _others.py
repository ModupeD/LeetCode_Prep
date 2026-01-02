class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        currLargest = max(nums)
        for i in range(len(nums)):
            if nums[i] < currLargest and nums[i]*2 > currLargest:
                return -1
        return nums.index(currLargest)