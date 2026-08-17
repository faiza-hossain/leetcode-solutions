from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        # Prefix sums
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dp(i, j):
            if i >= j:
                return 0

            ans = 0
            left = 0
            right = prefix[j + 1] - prefix[i]

            for k in range(i, j):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    # Bob removes right
                    if ans >= left * 2:
                        continue

                    ans = max(ans, left + dp(i, k))

                elif left > right:
                    # Bob removes left
                    if ans >= right * 2:
                        break

                    ans = max(ans, right + dp(k + 1, j))

                else:
                    # Equal: Alice chooses
                    ans = max(
                        ans,
                        left + dp(i, k),
                        right + dp(k + 1, j)
                    )

            return ans

        return dp(0, n - 1)
