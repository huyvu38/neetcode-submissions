class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for u, v, w in times:
            if u not in adj:
              adj[u] = []
            adj[u].append((v, w))

        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, time):
            if time >= dist[node]:
                return
            
            dist[node] = time
            
            for nei, w in adj.get(node, []):
                dfs(nei, time + w)
        
        #k is the source node
        dfs(k, 0)

        res = max(dist.values())
        if res < float("inf"):
            return res
        return -1