from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        subsets = [] 
        for mask in range(1, 1 << n):
            cur_lcm = 1
            size = 0
            for i in range(n):
                if mask & (1 << i):
                    cur_lcm = cur_lcm * coins[i] // gcd(cur_lcm, coins[i])
                    size += 1
            subsets.append((cur_lcm, size))
        
        def count_leq(x: int) -> int:
            total = 0
            for lcm_val, size in subsets:
                if size % 2 == 1: 
                    total += x // lcm_val
                else:            
                    total -= x // lcm_val
            return total
        
        # Binary search for the k-th smallest value
        left, right = 1, min(coins) * k
        while left < right:
            mid = (left + right) // 2
            if count_leq(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left