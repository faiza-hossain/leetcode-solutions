
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[set() for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                x = grid[i][j]

                if i == 0 and j == 0:
                    dp[i][j].add(x)
                    continue

                prev = set()

                if i > 0:
                    prev |= dp[i - 1][j]

                if j > 0:
                    prev |= dp[i][j - 1]

                dp[i][j] = {v ^ x for v in prev}

        return min(dp[m - 1][n - 1])
