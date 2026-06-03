class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        #calculate distance between any 2 points
        adj = {i: [] for i in range(n)}
        for i in range(n-1):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visit = set()
        #start from first point
        minHeap = [[0, 0]]
        while len(visit) < n:
            distance, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            res += distance
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [neiCost, nei])
        return res