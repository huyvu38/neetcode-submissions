class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def dfs(path, index):
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return
            for i in range(index, len(candidates)):
                #blocks generating the same combination twice at the same recursion level.
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                dfs(path, i+1)
                path.pop()
        dfs([], 0)
        return res
        