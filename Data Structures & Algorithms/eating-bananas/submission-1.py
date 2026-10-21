import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        big = max(piles)


        l = 1
        r = big

        while l < r:
            mid = (l+r)//2

            hour = 0
            for i in range(len(piles)):
                hour+= math.ceil(piles[i]/mid)
            if hour <= h:
                r = mid
            else:
                l = mid + 1
        return l
        