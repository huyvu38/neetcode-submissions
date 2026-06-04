from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges):

        graph = defaultdict(list)

        def dfs(src, target, visited):
            if src == target:
                return True

            visited.add(src)

            for nei in graph[src]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True

            return False

        for u, v in edges:

            # check if u can already reach v
            if u in graph and v in graph and dfs(u, v, set()):
                return [u, v]

            # otherwise add edge
            graph[u].append(v)
            graph[v].append(u)