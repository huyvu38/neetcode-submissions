class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        low = intervals[0][0]
        high =intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > high:
              res.append([low, high])
              low = intervals[i][0]
              high = intervals[i][1]
            else:
              #compare 2 high
              high = max(high, intervals[i][1])
        #Append last
        res.append([low,high])
        return res