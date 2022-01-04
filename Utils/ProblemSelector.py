from abc import ABC, abstractmethod

from LinearProgram import LinearProgram


class ProblemSelector(ABC):
    @abstractmethod
    def select(self, problems: list[LinearProgram]) -> (LinearProgram, list[LinearProgram]):
        pass


class LIFOSelector(ProblemSelector):
    def select(self, problems: list[LinearProgram]) -> (LinearProgram, list[LinearProgram]):
        selected = problems.pop()
        return selected, problems


class MaxUpperBoundSelector(ProblemSelector):
    def select(self, problems: list[LinearProgram]) -> (LinearProgram, list[LinearProgram]):
        best_problem = None
        best_function_value = float("inf")
        for problem in problems:
            x = problem.solve()[1]
            if x <= best_function_value:
                best_function_value = x
                best_problem = problem

        problems.remove(best_problem)
        return best_problem, problems


