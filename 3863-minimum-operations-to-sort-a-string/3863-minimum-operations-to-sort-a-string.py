class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        if s==''.join(sorted(s)):
            return 0
        if n==2:
            return -1
        minnn=min(s)
        maxxx=max(s)
        if s[0]==minnn or s[-1]==maxxx:
            return 1
        if any(c == minnn or c == maxxx for c in s[1:-1]):
            return 2

        return 3

