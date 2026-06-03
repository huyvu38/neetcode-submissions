class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        low, high = newInterval
        inserted = False
        for start, end in intervals:
            # Case 1: Current interval is completely before new interval
            if end < low:
                result.append([start, end])
            # Case 2: Current interval is completely after new interval
            elif start > high:
                if not inserted:
                    result.append([low, high])
                result.append([start, end])
                inserted = True
            
            # Case 3: merge if overlap
            else:
                low = min(low, start)
                high = max(high, end)
        
        # If new interval not add -> add to last
        if not inserted:
            result.append([low, high])
        
        return result