from abc import ABC, abstractmethod

from LinearProgram import LinearProgram


class ProblemSelector(ABC):
    @abstractmethod
    def select(self, problems: list[LinearProgram]) -> (LinearProgram, list[LinearProgram]):
        pass


class LIFOSelector(ProblemSelector):
    def select(self, problems: list[LinearProgram]) -> (LinearProgram, list[LinearProgram]):
        pass


class MaxUpperBoundSelector(ProblemSelector):
    def select(self, problems: list[LinearProgram]) -> (LinearProgram, list[LinearProgram]):
        pass
