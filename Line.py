from dataclasses import dataclass


@dataclass
class Line:
    x1: float
    y1: float

    x2: float
    y2: float

    def first_point(self):
        return self.x1, self.y1

    def second_point(self):
        return self.x2, self.y2
