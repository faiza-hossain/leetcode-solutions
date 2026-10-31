from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = 1

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    if dp[i][j][0] and i + 1 < m:
                        dp[i + 1][j][1] = (
                            dp[i + 1][j][1] + dp[i][j][0]
                        ) % MOD

                    if dp[i][j][1] and j + 1 < n:
                        dp[i][j + 1][0] = (
                            dp[i][j + 1][0] + dp[i][j][1]
                        ) % MOD

                else:
                    ways = (dp[i][j][0] + dp[i][j][1]) % MOD

                    if j + 1 < n:
                        dp[i][j + 1][0] = (
                            dp[i][j + 1][0] + ways
                        ) % MOD

                    if i + 1 < m:
                        dp[i + 1][j][1] = (
                            dp[i + 1][j][1] + ways
                        ) % MOD

        return sum(dp[m - 1][n - 1]) % MOD