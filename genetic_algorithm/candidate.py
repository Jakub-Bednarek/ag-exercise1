import copy
import random

from genetic_algorithm.helpers.data_loader import DataEntry
from typing import Tuple


class InvalidBackpackEntriesSizeException(Exception):
    pass


class Candidate:
    POSITIVE_BIT_GENERATION_CHANCE = 0.001

    def __init__(self, chromosomes: list[bool], mutation_probability: float):
        self.chromosomes: list[bool] = chromosomes
        self.chromosomes_count: int = len(self.chromosomes)
        self.adaptation_score: float = 0.0
        self.weight_carried: float = 0.0
        self.mutation_probability: float = mutation_probability

    def calculate_adaptation_score(
        self, backpack_entries: list[DataEntry], backpack_limit: float
    ) -> float:
        if not self.__are_backpack_entries_valid(backpack_entries):
            raise InvalidBackpackEntriesSizeException()

        total_weight, adaptation_score = self.__calculate_weight_and_adaptation(
            backpack_entries
        )
        if not total_weight > backpack_limit:
            self.adaptation_score = adaptation_score
            self.weight_carried = total_weight
        else:
            self.adaptation_score = 0.0
            self.weight_carried = 0.0
            adaptation_score = 0.0

        return adaptation_score

    def mutate(self):
        self.chromosomes = [
            (
                not chromosome
                if random.random() < self.mutation_probability
                else chromosome
            )
            for chromosome in self.chromosomes
        ]

    def crossover(self, other_parent, double_point_crossover_enabled: bool):
        if double_point_crossover_enabled:
            return self.__double_point_crossover(other_parent)
        else:
            return self.__single_point_crossover(other_parent)

    def get_adaptation_score(self) -> float:
        return self.adaptation_score

    def __calculate_weight_and_adaptation(
        self, backpack_entries: list[DataEntry]
    ) -> Tuple[float, float]:
        total_weight = 0.0
        adaptation_score = 0.0
        for i in range(0, self.chromosomes_count):
            if self.chromosomes[i]:
                adaptation_score += backpack_entries[i].value
                total_weight += backpack_entries[i].weight

        return total_weight, adaptation_score

    def __are_backpack_entries_valid(self, backpack_entries: list[DataEntry]):
        return len(backpack_entries) == self.chromosomes_count

    def __single_point_crossover(self, other_parent):
        crossover_point = self.__generate_crossover_point()
        new_candidate = copy.deepcopy(self)

        new_candidate.chromosomes = (
            new_candidate.chromosomes[0:crossover_point]
            + other_parent.chromosomes[crossover_point:]
        )

        return new_candidate

    def __double_point_crossover(self, other_parent):
        first_crossover_point = self.__generate_crossover_point()
        second_crossover_point = first_crossover_point
        new_candidate = copy.deepcopy(self)

        while second_crossover_point == first_crossover_point:
            second_crossover_point = self.__generate_crossover_point()

        (
            first_crossover_point,
            second_crossover_point,
        ) = self.__get_sorted_crossover_points(
            first_crossover_point, second_crossover_point
        )

        new_candidate.chromosomes = (
            new_candidate.chromosomes[0:first_crossover_point]
            + other_parent.chromosomes[first_crossover_point:second_crossover_point]
            + new_candidate.chromosomes[second_crossover_point:]
        )

        return new_candidate

    # python list operator does not include upper bound of the range, safe to use full length
    def __generate_crossover_point(self) -> int:
        return random.randint(0, self.chromosomes_count - 1)

    def __get_sorted_crossover_points(
        self, first_crossover_point: int, second_crossover_point: int
    ) -> Tuple[int, int]:
        if first_crossover_point > second_crossover_point:
            swap_tmp = first_crossover_point
            first_crossover_point = second_crossover_point
            second_crossover_point = swap_tmp

        return first_crossover_point, second_crossover_point

    def __str__(self) -> str:
        return f"{self.adaptation_score} | {self.chromosomes}"

    def __repr__(self) -> str:
        return str(self)

    @staticmethod
    def generate_random(entries_count: int, mutation_probability: float):
        generated_chromosomes: list[bool] = []
        for i in range(0, entries_count):
            random_value = random.random()
            generated_chromosomes.append(
                random_value < Candidate.POSITIVE_BIT_GENERATION_CHANCE
            )

        return Candidate(generated_chromosomes, mutation_probability)
