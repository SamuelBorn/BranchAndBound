import math
import tkinter as tk

import Utils2D
from Line import Line
from LinearProgram import LinearProgram

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from matplotlib.patches import Polygon


def draw_graph(lin_prog: LinearProgram, frame: tk.Frame):
    assert len(lin_prog.minimize_function) == 2

    fig = Figure(figsize=(7, 5))
    my_plot = fig.add_subplot(111)

    from scipy.spatial import ConvexHull
    points = np.array(Utils2D.get_valid_intersections(lin_prog.constraints))
    hull = ConvexHull(points)
    my_plot.fill(points[hull.vertices, 0], points[hull.vertices, 1], 'lightblue', alpha=0.6)

    for line in get_lines(lin_prog):
        my_plot.plot(line.second_point(), line.first_point(), color="gray")

    max_x, max_y = __get_max_x_y__(get_lines(lin_prog))
    my_plot.axis([0, max_x + 1, 0, max_y + 1])

    x0, x1 = 0, max_x + 1
    y0, y1 = 0, max_y + 1
    X, Y = np.meshgrid(np.arange(round(x0), round(x1) + 1),
                       np.arange(round(y0), round(y1) + 1))
    my_plot.scatter(X, Y, s=2, c="lightgray")

    FigureCanvasTkAgg(fig, master=frame).get_tk_widget().pack(fill=tk.BOTH)


def get_lines(lin_prog: LinearProgram):
    lines = []
    for constraint in lin_prog.constraints:
        a, b, c = constraint  # ax + by = c
        if abs(a) <= 0.00001 or abs(b) <= 0.00001:
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
            lines.append(Line(0, c / b, max_x, c / b))
        elif abs(b) <= 0.0001:
            lines.append(Line(c / a, 0, c / a, max_y))

    return lines


# returns the extremes of x and y, so I know how long to draw lines parallel to the axis
def __get_max_x_y__(lines: list[Line]):
    max_x = 3
    max_y = 3
    for line in lines:
        if line.x1 > max_x:
            max_x = line.x1
        if line.x2 > max_x:
            max_x = line.x2
        if line.y1 > max_y:
            max_y = line.y1
        if line.y2 > max_y:
            max_y = line.y2
    return max_x, max_y
