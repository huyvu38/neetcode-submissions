class CountSquares:

    def __init__(self):
        self.pts = []
        self.pts_count = {}

    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        key = tuple(point)
        self.pts_count[key] = self.pts_count.get(key, 0) + 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for x, y in self.pts:
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue

            res += self.pts_count.get((x, py), 0) * self.pts_count.get((px, y), 0)

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()