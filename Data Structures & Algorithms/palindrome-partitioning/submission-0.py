class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def is_palindrome(string):
            for i in range(len(string) // 2):
                if string[i] != string[len(string) - 1 - i]:
                    return False
            return True

        res = []

        def backtrack(path, index):
            if index == len(s):
                res.append(path[:]) 
                return

            for i in range(index + 1, len(s) + 1):
                substring = s[index:i]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(path, i)
                    path.pop()

        backtrack([], 0)
        return res
