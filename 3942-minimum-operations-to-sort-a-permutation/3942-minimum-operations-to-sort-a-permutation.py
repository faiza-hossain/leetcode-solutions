
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')

        if all(nums[i] == (nums[0] + i) % n for i in range(n)):
            k = nums[0]
            ans = min(ans, (n - k) % n, k + 2)

        if all(nums[i] == (nums[0] - i) % n for i in range(n)):
            k = (n - 1 - nums[0]) % n
            ans = min(ans, 1 + min(k, (n - k) % n))

        return ans if ans != float('inf') else -1
