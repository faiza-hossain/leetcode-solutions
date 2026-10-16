class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node: int, l: int, r: int) -> None:
            if lazy[node] != 0:
                val = lazy[node]
                mid = (l + r) // 2
                
                left_len = mid - l + 1
                tree_sq[2 * node] = (tree_sq[2 * node] + 2 * val * tree_sum[2 * node] + left_len * val * val) % MOD
                tree_sum[2 * node] = (tree_sum[2 * node] + left_len * val) % MOD
                lazy[2 * node] += val
                
                right_len = r - mid
                tree_sq[2 * node + 1] = (tree_sq[2 * node + 1] + 2 * val * tree_sum[2 * node + 1] + right_len * val * val) % MOD
                tree_sum[2 * node + 1] = (tree_sum[2 * node + 1] + right_len * val) % MOD
                lazy[2 * node + 1] += val
                
                lazy[node] = 0

        def update(node: int, l: int, r: int, ql: int, qr: int) -> None:
            if ql <= l and r <= qr:
                length = r - l + 1
                tree_sq[node] = (tree_sq[node] + 2 * tree_sum[node] + length) % MOD
                tree_sum[node] = (tree_sum[node] + length) % MOD
                lazy[node] += 1
                return
            
            push(node, l, r)
            mid = (l + r) // 2
            
            if ql <= mid:
                update(2 * node, l, mid, ql, qr)
            if qr > mid:
                update(2 * node + 1, mid + 1, r, ql, qr)
                
            tree_sum[node] = (tree_sum[2 * node] + tree_sum[2 * node + 1]) % MOD
            tree_sq[node] = (tree_sq[2 * node] + tree_sq[2 * node + 1]) % MOD

        last_seen = {}
        total_ans = 0
        
        for i, val in enumerate(nums):
            prev_idx = last_seen.get(val, -1)
            update(1, 0, n - 1, prev_idx + 1, i)
            last_seen[val] = i
            total_ans = (total_ans + tree_sq[1]) % MOD

        return total_ans