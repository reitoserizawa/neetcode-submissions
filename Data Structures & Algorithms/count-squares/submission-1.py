class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for (x, y), cnt in self.points.items():
            if abs(py - y) != abs(px-x) or x == px or y == py:
                continue
            res += (
                self.points.get((x, py), 0) *
                self.points.get((px, y), 0) *
                cnt
            )

        return res



        


        
