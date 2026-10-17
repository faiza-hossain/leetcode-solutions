class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def digit_sum(x):
            return sum(map(int, str(x)))

        n = len(nums)
        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {x: i for i, x in enumerate(arr)}
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle = 0

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle += 1

            swaps += max(0, cycle - 1)

        return swaps