class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        res = set()

        def dfs(exp: str) -> None:
            j = exp.find('}')
            
            if j == -1:
                res.add(exp)
                return
            
            i = exp.rfind('{', 0, j)
            
            left = exp[:i]
            right = exp[j + 1:]
            
            for option in exp[i + 1:j].split(','):
                dfs(left + option + right)

        dfs(expression)
        return sorted(list(res))