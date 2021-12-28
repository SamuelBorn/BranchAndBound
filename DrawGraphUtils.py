import math
import tkinter as tk

from Line import Line
from LinearProgram import LinearProgram


def draw_graph(lin_prog: LinearProgram, frame: tk.Frame):
    assert len(lin_prog.minimize_function) == 2


def get_lines(lin_prog: LinearProgram):
    lines = []
    for constraint in lin_prog.constraints:
        a, b, c = constraint  # ax + by = c
        if abs(a) <= 0.00001 and abs(b) <= 0.00001:
            continue

        #  x = 0
        y1 = c / b
        x1 = (c - b * y1) / a

        #  y = 0
        x2 = c / a
        y2 = (c - a * x2) / b

        lines.append(Line(x1, y1, x2, y2))

    max_x, max_y = __get_max_x_y__(lines)

    for constraint in lin_prog.constraints:
        a, b, c = constraint  # ax + by = c
        if abs(a) <= 0.0001:
            lines.append()

# returns the extremes of x and y, so I know how long to draw lines parallel to the axis
def __get_max_x_y__(lines: list(Line)):
    max_x = 3
    max_y = 3
    for line in lines:
        if line.x1 > max_x:
            max_x = line.x1
        if line.x2 > max_x:
            max_x = line.x2
        if line.y1 > may_y:
            may_y = line.y1
        if line.y2 > may_y:
            may_y = line.y2
    return max_x, max_y
