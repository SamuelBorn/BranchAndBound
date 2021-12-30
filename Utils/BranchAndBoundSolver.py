from tkinter import Frame

import math

from LinearProgram import LinearProgram
from Utils import Utils2D, DrawEquationUtil, DrawGraphUtil
from Utils.ProblemSelector import ProblemSelector


class BranchAndBoundSolver:
    def __init__(self, start: LinearProgram, frame: Frame, selection_rule: ProblemSelector) -> None:
        self.L: list[LinearProgram] = [start]
        self.Fl: float = float("inf")
        self.frame = frame
        self.selection_rule = selection_rule

    def solve(self):
        while self.L:
            P: LinearProgram
            P, self.L = self.selection_rule.select(self.L)

            DrawEquationUtil.draw_equations(P, self.frame)
            DrawGraphUtil.draw_graph(P, self.frame)

            optimal_point, optimal_value = P.solve()

            if self.ausgelotet(optimal_point, optimal_value):
                pass  # already removed P from L in problem selector
                print("ausgelotet")
            else:
                for idx, optimal_point_value in enumerate(optimal_point):
                    if not Utils2D.almost_integer(optimal_point_value):
                        new_upper_constraint = [0] * (len(optimal_point) + 1)
                        new_upper_constraint[-1] = -math.ceil(optimal_point_value)
                        new_upper_constraint[idx] = -1
                        print(
                            LinearProgram(P.constraints + [new_upper_constraint], P.minimize_function, P.was_maximize))
                        self.L.append(
                            LinearProgram(P.constraints + [new_upper_constraint], P.minimize_function, P.was_maximize))

                        new_lower_constraint = [0] * (len(optimal_point) + 1)
                        new_lower_constraint[-1] = math.floor(optimal_point_value)
                        new_lower_constraint[idx] = 1
                        print(
                            LinearProgram(P.constraints + [new_lower_constraint], P.minimize_function, P.was_maximize))
                        self.L.append(
                            LinearProgram(P.constraints + [new_lower_constraint], P.minimize_function, P.was_maximize))

        print(self.Fl)

    def ausgelotet(self, optimal_point, optimal_value):
        if optimal_value >= self.Fl:
            return True
        if optimal_point is None:
            return True
        if Utils2D.is_integer_vector(optimal_point):
            self.Fl = optimal_value
            return True
        return False
