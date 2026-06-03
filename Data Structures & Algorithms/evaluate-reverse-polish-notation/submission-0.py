class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #res = 0
        stack=[]
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                newValue=0
                secondElement = stack.pop()
                firstElement = stack.pop()
                if token == '*':
                    newValue=firstElement * secondElement
                elif token == '/':
                    newValue=int(firstElement / secondElement)
                elif token == '+':
                    newValue=firstElement + secondElement
                elif token == '-':
                    newValue=firstElement - secondElement
                stack.append(newValue)
        return stack[0]