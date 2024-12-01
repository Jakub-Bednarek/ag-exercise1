from abc import ABC, abstractmethod
from enum import Enum, auto
from genetic_algorithm.candidate import Candidate


class AdaptationFunctionType(Enum):
    ROULETTE = auto()
    TOURNAMENT = auto()
    RANKING = auto()


class AdaptationFunctionBase(ABC):
    @abstractmethod
    def select(self, candidates: list[Candidate]):
        pass


class RouletteSelectionFunction(AdaptationFunctionBase):
    def select(self, candidates: list[Candidate]):
        return candidates


class TournamentSelectionFunction(AdaptationFunctionBase):
    def select(self, candidates: list[Candidate]):
        return candidates


class RankingSelectionFunction(AdaptationFunctionBase):
    def select(self, candidates: list[Candidate]):
        return candidates


class AdaptationFunctionFactory:
    @staticmethod
    def create(type: AdaptationFunctionType):
        return RankingSelectionFunction()
