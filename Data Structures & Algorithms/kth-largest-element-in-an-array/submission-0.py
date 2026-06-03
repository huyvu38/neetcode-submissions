class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        value = 0
        while k > 0:
            value = heapq.heappop(max_heap)
            k = k-1
        return -value
        