class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(index, path):
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(i, path)
                path.pop()
        dfs(0, [])
        return res