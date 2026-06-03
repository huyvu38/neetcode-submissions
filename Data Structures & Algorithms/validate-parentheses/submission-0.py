class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack=[]
        for char in s:
            if char == '{' or char == '(' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last_char = stack.pop()
                if last_char == '(' and char != ")":
                   return False
                elif last_char == '[' and char != "]":
                   return False
                elif last_char == '{' and char != "}":
                   return False
        return len(stack) == 0