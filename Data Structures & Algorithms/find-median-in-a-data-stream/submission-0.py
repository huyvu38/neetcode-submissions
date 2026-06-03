class MedianFinder(object):

    def __init__(self):
        self.small = []
        self.large= []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -num) #max_heap
        heapq.heappush(self.large, -heapq.heappop(self.small)) #min_heap

        # balance sizes (small can have at most 1 extra)
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        :rtype: float
        """

        if len(self.small) > len(self.large):
            # small has the extra element 
            # since small is max_heap and all value in small < large
            return float(-self.small[0])
        else:
            # even number of elements
            return (-self.small[0] + self.large[0]) / 2.0