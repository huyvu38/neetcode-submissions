class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        max_heap = []
        for stone in stones:
           heapq.heappush(max_heap, -stone)  # store negative
        while len(max_heap) > 1:
            #Get 2 largest
            first =  heapq.heappop(max_heap)
            second =  heapq.heappop(max_heap)
    
            #second will be smaller weight
            compare = abs(first) - abs(second)
            if compare > 0:
                heapq.heappush(max_heap, -compare)
        if len(max_heap) == 0:
            return 0
        return abs(max_heap[0])