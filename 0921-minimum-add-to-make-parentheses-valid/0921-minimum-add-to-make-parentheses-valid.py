class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        add_needed = 0
        for char in s:
            if char == '(':
                open_count += 1
            elif char == ')':
                if open_count > 0:
                    open_count -= 1
                else:
                    add_needed += 1
        return open_count + add_needed