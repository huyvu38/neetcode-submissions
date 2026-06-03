class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        min_heap = []
        for point in points:
            x= point[0]
            y=point[1]
            distance = math.sqrt(x ** 2 + y ** 2)
            min_heap.append([distance,x,y])
        heapq.heapify(min_heap)
        res=[]
        for i in range(0,k):
            smallest = heapq.heappop(min_heap)
            res.append([smallest[1], smallest[2]])
        return res
        