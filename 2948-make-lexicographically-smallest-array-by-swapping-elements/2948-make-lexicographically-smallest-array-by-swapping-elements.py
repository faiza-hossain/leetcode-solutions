class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        idx = sorted(range(n), key=lambda i: nums[i])
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for i in range(1, n):
            if nums[idx[i]] - nums[idx[i - 1]] <= limit:
                union(idx[i], idx[i - 1])

        groups = {}
        for i in idx:
            groups.setdefault(find(i), []).append(i)

        ans = [0] * n
        for root, positions in groups.items():
            positions.sort()
            values = sorted(nums[p] for p in positions)
            for p, v in zip(positions, values):
                ans[p] = v

        return ans