import functools

class Solution:

  def hasValidPath(self, grid: list[list[str]]) -> bool:
    m, n = len(grid), len(grid[0])

    if (m + n - 1) % 2 != 0:
      return False
    if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
      return False

    @functools.lru_cache(None)
    def dfs(i, j, balance):
      if grid[i][j] == '(':
        balance += 1
      else:
        balance -= 1

      if balance < 0:
        return False

      remaining_steps = (m - 1 - i) + (n - 1 - j)
      if balance > remaining_steps:
        return False

      if i == m - 1 and j == n - 1:
        return balance == 0

      move_down = False
      move_right = False

      if i + 1 < m:
        move_down = dfs(i + 1, j, balance)
      if j + 1 < n:
        move_right = dfs(i, j + 1, balance)

      return move_down or move_right

    return dfs(0, 0, 0)