class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count = count + 1
                else:
                    count = count -1
                #get rid immediately
                if count < 0:
                    return False
            if count == 0:
                return True
            return False
        def dfs(s):
            if n * 2 == len(s):
                if valid(s):
                    res.append(s)
                return
            
            dfs(s + '(')
            dfs(s + ')')
        
        dfs("")
        return res