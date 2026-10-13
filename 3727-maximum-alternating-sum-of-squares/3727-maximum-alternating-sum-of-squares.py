class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        positive = sum(x * x for x in nums[n // 2:])
        negative = sum(x * x for x in nums[:n // 2])

        return positive - negative