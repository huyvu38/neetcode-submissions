class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            k = (l + r) // 2
            total_time = 0
            for pile in piles:
                time = math.ceil(pile / k)
                total_time = total_time + time
            if total_time > h:
                l = k+1
            else:
                r= k-1
        return l