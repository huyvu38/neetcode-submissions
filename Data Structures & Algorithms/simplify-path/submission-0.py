class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        parts = path.split("/")
        for part in parts:
            #Skip for first ""  or "." since it just parent directory
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    #go back to previous dir
                    stack.pop()
            else:
                stack.append(part)
        #Always have / at beginning
        return "/" + "/".join(stack)