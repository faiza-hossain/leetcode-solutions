class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current_string, open_count, close_count):
            if len(current_string) == 2 * n:
                result.append("".join(current_string))
                return
            
            if open_count < n:
                current_string.append('(')
                backtrack(current_string, open_count + 1, close_count)
                current_string.pop()  
                
            if close_count < open_count:
                current_string.append(')')
                backtrack(current_string, open_count, close_count + 1)
                current_string.pop()  
                
        backtrack([], 0, 0)
        return result