class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num: return ""
        nines, rem = divmod(sum, 9)
        if rem > 0:
            return "9" * nines + str(rem) + "0" * (num - nines - 1)
        return "9" * nines + "0" * (num - nines)