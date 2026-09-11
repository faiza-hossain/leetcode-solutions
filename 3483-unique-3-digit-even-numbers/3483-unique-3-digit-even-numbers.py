from typing import List
import itertools

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_numbers = set()
        
        for a, b, c in itertools.permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                unique_numbers.add(a * 100 + b * 10 + c)
                
        return len(unique_numbers)