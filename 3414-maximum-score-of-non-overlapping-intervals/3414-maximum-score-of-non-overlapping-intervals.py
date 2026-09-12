from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        events = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)])
        starts = [e[0] for e in events]
        
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            l, r, w, orig_idx = events[i]
            next_idx = bisect_right(starts, r)
            
            for k in range(1, 5):
                skip = dp[i + 1][k]
                
                prev_neg_w, prev_tuple = dp[next_idx][k - 1]
                take = (prev_neg_w - w, tuple(sorted(prev_tuple + (orig_idx,))))
                
                dp[i][k] = min(skip, take)
                
        return list(dp[0][4][1])