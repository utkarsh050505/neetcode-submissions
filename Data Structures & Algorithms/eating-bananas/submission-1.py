import math
from typing import List

class Solution:
    def is_ans(self, piles: List[int], can_h: int, h: int) -> bool:
        took = 0
        for i in piles:
            # Integer math for ceiling division: math.ceil(i / can_h)
            took += (i + can_h - 1) // can_h
        return took <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Koko must eat at least 1 banana per hour
        left = 1 
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            if self.is_ans(piles, mid, h):
                # mid is a possible answer, look for smaller speeds
                right = mid  
            else:
                # mid is too slow, speed up
                left = mid + 1 
                
        return left
