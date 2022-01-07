from tkinter import Frame

import math

import tkinter as tk

from LinearProgram import LinearProgram
from Utils import Utils2D, DrawEquationUtil, DrawGraphUtil
from Utils.ProblemSelector import ProblemSelector


class BranchAndBoundSolver:
    def __init__(self, start: LinearProgram, frame: Frame, selection_rule: ProblemSelector,
                 show_integer_points) -> None:
        self.L: list[LinearProgram] = [start]
        self.Fl: float = float("inf")
        self.opt: list[float] = None
        self.frame = frame
        self.selection_rule = selection_rule
        self.draw_enabled = len(start.minimize_function) == 2
        self.was_max_factor = -1 if start.was_maximize else 1
        self.show_integer_points = show_integer_points

    def solve(self):
        while self.L:
            P: LinearProgram
            P, self.L = self.selection_rule.select(self.L)

            DrawEquationUtil.draw_equations(P, self.frame)

            if self.draw_enabled:
                DrawGraphUtil.draw_graph(P, self.frame, self.show_integer_points)

            optimal_point, optimal_value = P.solve()

            if self.ausgelotet(optimal_point, optimal_value):
                pass  # already removed P from L in problem selector
            else:
                for idx, optimal_point_value in enumerate(optimal_point):
                    if not Utils2D.almost_integer(optimal_point_value):
                        new_upper_constraint = [0] * (len(optimal_point) + 1)
                        new_upper_constraint[-1] = -math.ceil(optimal_point_value)
                        new_upper_constraint[idx] = -1
                        self.L.append(
                            LinearProgram(P.constraints + [new_upper_constraint], P.minimize_function, P.was_maximize))

                        new_lower_constraint = [0] * (len(optimal_point) + 1)
                        new_lower_constraint[-1] = math.floor(optimal_point_value)
                        new_lower_constraint[idx] = 1
                        self.L.append(
                            LinearProgram(P.constraints + [new_lower_constraint], P.minimize_function, P.was_maximize))
                        break

            h_line = "_" * 200
            tk.Label(self.frame, text=h_line, font='Helvetica 30 bold', fg="black", bg="white").pack()

        o = self.was_max_factor * self.Fl
        l = round(o) if Utils2D.almost_integer(o) else o
        tk.Label(self.frame, text=f"\n\n\n\nDer optimale ganzzahlige Wert ist:     {l}",
                 font='Helvetica 14 bold', bg="white").pack()
        DrawEquationUtil.draw_int_vec(self.opt, self.frame)
        tk.Label(self.frame, text="\n", bg="white").pack()

    def ausgelotet(self, optimal_point, optimal_value):
        if optimal_point is None:
            tk.Label(self.frame, text=f"ausgelotet, da Lösungsmenge leer", bg="white").pack()
            return True

        if optimal_value >= self.Fl:
            tk.Label(self.frame, text=f"ausgelotet, da {optimal_value} >= bisheriger bester Wert {self.Fl} ist", bg="white").pack()
            return True

        if Utils2D.is_integer_vector(optimal_point):
            self.Fl = optimal_value
            self.opt = optimal_point
            tk.Label(self.frame, text=f"ausgelotet, da neuer ganzzahliger Punkt gefunden wurde", bg="white").pack()
            return True

        return False
