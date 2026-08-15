class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = 0
        for x in nums:
            total ^= x
        if total != 0:
            return len(nums)
        if all(x == 0 for x in nums):
            return 0
        return len(nums) - 1
        