from abc import ABC, abstractmethod
from enum import Enum, auto


class AdaptationFunctionType(Enum):
    ROULETTE = auto()
    TOURNAMENT = auto()
    RANKING = auto()


class AdaptationFunctionBase(ABC):
    @abstractmethod
    def evaluate(self):
        pass


class RouletteSelectionFunction(AdaptationFunctionBase):
    def evaluate(self):
        print("Roulette")


class TournamentSelectionFunction(AdaptationFunctionBase):
    def evalutate(self):
        print("Tournament")


class RankingSelectionFunction(AdaptationFunctionBase):
    def evaluate(self):
        print("Ranking")


class AdaptationFunctionFactory:
    @staticmethod
    def create(type: AdaptationFunctionType):
        return RankingSelectionFunction()
