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

    def get_x(self):
        return self.x1, self.x2

    def get_y(self):
        return self.y1, self.y2
