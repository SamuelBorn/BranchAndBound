import tkinter as tk


from Line import Line
from LinearProgram import LinearProgram

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

from Utils import Utils2D


def draw_graph(lin_prog: LinearProgram, frame: tk.Frame):
    assert len(lin_prog.minimize_function) == 2

    fig = Figure(figsize=(7, 5))
    my_plot = fig.add_subplot(111)

    from scipy.spatial import ConvexHull  # color the constrained area
    points = np.array(Utils2D.get_valid_intersections(lin_prog.constraints))
    hull = ConvexHull(points)
    my_plot.fill(points[hull.vertices, 0], points[hull.vertices, 1], 'lightblue', alpha=0.6)

    for line in get_lines(lin_prog):  # draw all constraint lines
        my_plot.plot(line.get_x(), line.get_y(), color="gray")
        # my_plot.plot(line.second_point(), line.first_point(), color="gray")

    max_x, max_y = __get_max_x_y__(get_lines(lin_prog))  # set the axis
    my_plot.axis([0, max_x + 1, 0, max_y + 1])

    x, y = np.meshgrid(np.arange(0, max_x + 1), np.arange(0, max_y + 1))  # draw all integer points
    my_plot.scatter(x, y, s=2, c="lightgray")

    target_line = get_target_function_line(lin_prog)
    my_plot.plot(target_line.get_x(), target_line.get_y(), color="orange")

    FigureCanvasTkAgg(fig, master=frame).get_tk_widget().pack(fill=tk.BOTH)  # add image to frame


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
            lines.append(Line(max_x + 0.5, c / b, 0, c / b))
        elif abs(b) <= 0.0001:
            lines.append(Line(c / a, max_y + 0.5, c / a, 0))

    return lines


def get_target_function_line(lin_prog: LinearProgram):
    optimal_point, optimal_value = lin_prog.solve()

    a, b = lin_prog.minimize_function  # ax + by
    c = optimal_value

    max_x, max_y = __get_max_x_y__(get_lines(lin_prog))
    if abs(a) <= 0.00001:
        return Line(0, c / b, max_x, c / b)
    elif abs(b) <= 0.0001:
        return Line(c / a, 0, c / a, max_y)
    else:
        y1 = c / b  # x = 0
        x1 = (c - b * y1) / a
        x2 = c / a  # y = 0
        y2 = (c - a * x2) / b
        return Line(x1, y1, x2, y2)


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
