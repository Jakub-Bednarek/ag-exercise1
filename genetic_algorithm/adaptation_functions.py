from abc import ABC, abstractmethod
from enum import Enum, auto
from genetic_algorithm.candidate import Candidate

import random


class EmptyCandidatesListException(Exception):
    pass


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


class AdaptationFunctionBase(ABC):
    @abstractmethod
    def select(self, candidates: list[Candidate]):
        pass


class RouletteSelectionFunction(AdaptationFunctionBase):
    def select(self, candidates: list[Candidate]):
        if len(candidates) == 0:
            raise EmptyCandidatesListException()

        weights, indexes, weight_total = self.__create_weights_and_indexes(candidates)
        if weight_total == 0:
            return candidates

        selected_candidates_indexes = random.choices(
            indexes, weights, k=len(candidates)
        )

        return [candidates[index] for index in selected_candidates_indexes]

    def __create_weights_and_indexes(self, sorted_candidates: list[Candidate]):
        weight_total = 0
        weights = []
        indexes = []
        for i, candidate in enumerate(sorted_candidates):
            weights.append(candidate.get_adaptation_score())
            indexes.append(i)
            weight_total += candidate.get_adaptation_score()

        return weights, indexes, weight_total


class TournamentSelectionFunction(AdaptationFunctionBase):
    def select(self, candidates: list[Candidate]):
        if len(candidates) == 0:
            raise EmptyCandidatesListException()

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
            if (
                candidates[candidate_index].get_adaptation_score()
                >= highest_adaptation_score
            ):
                highest_adaptation_score = candidates[
                    candidate_index
                ].get_adaptation_score()
                winning_candidate_index = candidate_index

        return candidates[winning_candidate_index]


class RankSelectionFunction(AdaptationFunctionBase):
    def select(self, candidates: list[Candidate]):
        if len(candidates) == 0:
            raise EmptyCandidatesListException()

        candidates.sort(key=lambda x: x.get_adaptation_score(), reverse=True)

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
