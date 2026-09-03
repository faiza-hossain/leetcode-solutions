class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = min_even = None
        for x in nums1:
            if x % 2:
                if min_odd is None or x < min_odd:
                    min_odd = x
            else:
                if min_even is None or x < min_even:
                    min_even = x

        p0 = min_odd is None                              
        p1 = min_even is None or (min_odd is not None and min_odd < min_even)

        return p0 or p1