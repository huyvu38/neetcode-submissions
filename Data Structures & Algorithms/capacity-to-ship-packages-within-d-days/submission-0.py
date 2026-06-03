class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Capacity need to be at least = max weights[i]
        l, r = max(weights), sum(weights)
        while l <= r:
            mid = (l + r) // 2
            #At least 1 day
            day = 1
            each_day = 0
            for w in weights:
                if each_day + w > mid:
                    each_day = w
                    day = day + 1
                else:
                    each_day = each_day + w
            #Need less day so need to improve capacity
            if day > days:
                l = mid + 1
            else:
                #Try to find min capacity within [1,days]
                r = mid - 1
        return l
            
