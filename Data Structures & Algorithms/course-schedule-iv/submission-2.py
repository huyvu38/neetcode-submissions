from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        # memo[u][v] = whether u can reach v
        memo = {}

        def dfs(node, target):
            if (node, target) in memo:
                return memo[(node, target)]

            if node == target:
                return True

            for nei in graph[node]:
                if dfs(nei, target):
                    memo[(node, target)] = True
                    return True

            memo[(node, target)] = False
            return False

        res = []
        for u, v in queries:
            res.append(dfs(u, v))

        return res