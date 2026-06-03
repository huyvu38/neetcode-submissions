class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0] * len(temperatures)
        for index, value in enumerate(temperatures):
            #loop while stack is not empty
            #remove from the stack all of element with value less than newest value
            while stack and stack[-1][1] < value:
                element = stack.pop()
                prev_index=element[0]
                res[prev_index]=index-prev_index
            stack.append([index,value])
        return res