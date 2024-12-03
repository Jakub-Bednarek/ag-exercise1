from abc import ABC, abstractmethod
from enum import Enum, auto
from genetic_algorithm.candidate import Candidate

import random


class AdaptationFunctionType(Enum):
    ROULETTE = auto()
    TOURNAMENT = auto()
    RANK = auto()

    @staticmethod
    def argparse(val):
        try:
            return AdaptationFunctionType[val]
        except KeyError:
            return s


# TODO: add random() as parameter to mock in UTs


class AdaptationFunctionBase(ABC):
    @abstractmethod
    def select(self, candidates: list[Candidate]):
        pass


class RouletteSelectionFunction(AdaptationFunctionBase):
    def select(self, candidates: list[Candidate]):
        candidates.sort(key=lambda x: x.adaptation_score)

        weights, indexes = self.__create_weights_and_indexes(candidates)
        if weights == 0:
            return candidates

        selected_candidates_indexes = random.choices(
            indexes, weights, k=len(candidates)
        )

        return [candidates[index] for index in selected_candidates_indexes]

    def __create_weights_and_indexes(self, sorted_candidates: list[Candidate]):
        weights = []
        indexes = []
        for i, candidate in enumerate(candidates):
            weights.append(candidate.adaptation_score)
            indexes.append(i)

        return weights, indexes


class TournamentSelectionFunction(AdaptationFunctionBase):
    def select(self, candidates: list[Candidate]):
        selected_candidates: list[Candidate] = []
        for i in range(0, len(candidates)):
            local_tournament_size = random.randint(1, len(candidates) - 1)

            tournament_winner = self.__evaluate_local_tournament(
                candidates, local_tournament_size
            )
            selected_candidates.append(tournament_winner)

        return selected_candidates

    def __evaluate_local_tournament(
        self, candidates: list[Candidate], tournament_size: int
    ):
        tournament_candidates_indexes: list[int] = list(range(0, len(candidates)))
        random.shuffle(tournament_candidates_indexes)

        local_tournament_winners = tournament_candidates_indexes[:tournament_size]
        highest_adaptation_score = 0
        winning_candidate_index = 0
        for candidate_index in local_tournament_winners:
            if candidates[candidate_index].adaptation_score > highest_adaptation_score:
                highest_adaptation_score = candidates[candidate_index].adaptation_score
                winning_candidate_index = candidate_index

        return candidates[winning_candidate_index]


class RankSelectionFunction(AdaptationFunctionBase):
    def select(self, candidates: list[Candidate]):
        candidates.sort(key=lambda x: x.adaptation_score)

        weights_and_indexes = [i for i in range(0, len(candidates))]

        selected_candidates_indexes = random.choices(
            weights_and_indexes,
            sorted(weights_and_indexes, reverse=True),
            k=len(candidates),
        )

        return [candidates[index] for index in selected_candidates_indexes]


class AdaptationFunctionFactory:
    @staticmethod
    def create(function_type: str):
        function_type = AdaptationFunctionType[function_type]
        match function_type:
            case AdaptationFunctionType.ROULETTE:
                return RouletteSelectionFunction()
            case AdaptationFunctionType.TOURNAMENT:
                return TournamentSelectionFunction()
            case AdaptationFunctionType.RANK:
                return RankSelectionFunction()
