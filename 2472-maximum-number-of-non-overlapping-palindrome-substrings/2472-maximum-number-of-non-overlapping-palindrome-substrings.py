class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        ans = 0
        last_end = -1
        n = len(s)
        
        for i in range(k - 1, n):
            if i - k + 1 > last_end and s[i - k + 1 : i + 1] == s[i - k + 1 : i + 1][::-1]:
                ans += 1
                last_end = i
            elif i - k > last_end and s[i - k : i + 1] == s[i - k : i + 1][::-1]:
                ans += 1
                last_end = i
                
        return ans