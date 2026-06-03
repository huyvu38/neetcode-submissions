class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        cars = []
        #sort from the closest to target then to farthest
        for i in range(0,len(position)):
           cars.append([position[i], speed[i]])
        cars.sort(key=lambda x: x[0], reverse=True)
        print(cars)
        stack=[]
        for car in cars:
            cur_pos, cur_speed =car[0], car[1]
            time=(target-cur_pos)/cur_speed
            #new fleet
            if len(stack) == 0 or stack[-1] < time:
                stack.append(time)
        return len(stack)