class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        numSum = sum(nums)
        leftSum = 0
        for i, v in enumerate(nums):
            if leftSum == numSum - leftSum - v:
                return i
            leftSum += v
        return -1

