class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)
        right = [0] * n
        right[-1] = nums[-1]

        for i in range(n-2,-1,-1):
            right[i] = min(nums[i], right[i + 1])

        left_max = nums[0]

        for i in range(n):
            left_max = max(left_max, nums[i])
            if left_max - right[i] <= k:
                return i

        return -1