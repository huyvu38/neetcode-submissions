class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #Init
        if target == "0000":
            return 0
        #Start already in deadend
        visited = set(deadends)
        if "0000" in visited:
            return -1

        queue = deque(["0000"])
        visited.add("0000")
        steps = 0

        while queue:
            steps += 1
            for _ in range(len(queue)):
                lock = queue.popleft()

                for i in range(4):
                    d = int(lock[i])

                    # Turn wheel up
                    if d == 9:
                        up = "0"
                    else:
                        up = str(d + 1)

                    nextLock = lock[:i] + up + lock[i + 1:]

                    if nextLock not in visited:
                        if nextLock == target:
                            return steps

                        visited.add(nextLock)
                        queue.append(nextLock)

                    # Turn wheel down
                    if d == 0:
                        down = "9"
                    else:
                        down = str(d - 1)

                    nextLock = lock[:i] + down + lock[i + 1:]

                    if nextLock not in visited:
                        if nextLock == target:
                            return steps

                        visited.add(nextLock)
                        queue.append(nextLock)
        return -1