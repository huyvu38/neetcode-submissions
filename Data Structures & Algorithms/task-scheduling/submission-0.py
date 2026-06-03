import heapq
from collections import deque
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        #Store frequency
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        
        #Store waiting in max heap
        max_heap = []
        for count in freq.values():
            heapq.heappush(max_heap, -count)
       
        #Store which need to cooldown
        cooldown = deque()
        time = 0
        while cooldown or max_heap:
            time+=1

            #Run task
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1  # +1 because negative
                if cnt != 0:
                    cooldown.append((time + n, cnt))
                # ==0 mean finish
            
            if cooldown and cooldown[0][0] == time:
                _, cnt = cooldown.popleft()
                heapq.heappush(max_heap, cnt)

        return time