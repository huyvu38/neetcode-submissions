class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            while len(stack) > 1:
                #Collide
                if stack[-1] < 0 and stack[-2] > 0:
                    last_asteroid = stack.pop()
                    near_last_asteroid = stack.pop()
                    if abs(last_asteroid) > abs(near_last_asteroid):
                        stack.append(last_asteroid)
                    elif abs(last_asteroid) == abs(near_last_asteroid):
                        continue
                    else:
                        stack.append(near_last_asteroid)
                else:
                    break
        return stack
