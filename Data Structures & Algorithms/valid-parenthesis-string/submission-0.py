class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0 #min of open parenthesis
        high = 0 #max of open parenthesis
        
        for c in s:
            if c == "(":
                low += 1
                high += 1
            elif c == ")":
                low -= 1
                high -= 1
            else:  # '*'
                low -= 1
                high += 1
            
            if high < 0:
                return False
            
            low = max(low, 0)
        
        return low == 0