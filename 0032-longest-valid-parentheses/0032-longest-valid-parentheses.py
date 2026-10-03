class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                
                if not stack:
                    stack.append(i)
                else:
                    current_len = i - stack[-1]
                    max_len = max(max_len, current_len)
                    
        return max_len