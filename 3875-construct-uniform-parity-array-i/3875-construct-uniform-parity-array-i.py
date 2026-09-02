class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        n = len(nums1)
        par = [x % 2 for x in nums1]

        def feasible(target: int) -> bool:
            for i in range(n):
                if par[i] == target:
                    continue
                need = par[i] ^ target
                if any(par[j] == need for j in range(n) if j != i):
                    continue
                return False
            return True

        return feasible(0) or feasible(1)