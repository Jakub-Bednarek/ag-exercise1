import random

from genetic_algorithm.helpers.data_loader import DataEntry


class InvalidBackpackEntriesSizeException(Exception):
    pass


# TODO: ex_2 MUTATION_PROBABILITY should be config param
class Candidate:
    MUTATION_PROBABILITY = 0.1

    def __init__(self, chromosomes: list[bool]):
        self.chromosomes: list[bool] = chromosomes
        self.chromosomes_count: int = len(self.chromosomes)
        self.adaptation_score: int = 0
        self.weight_carried: int = 0

    def calculate_adaptation_score(
        self, backpack_entries: list[DataEntry], backpack_limit: int
    ) -> int:
        if not self.__are_backpack_entries_valid(backpack_entries):
            raise InvalidBackpackEntriesSizeException()

        total_weight, adaptation_score = self.__calculate_weight_and_adaptation(
            backpack_entries
        )
        if not total_weight > backpack_limit:
            self.adaptation_score = adaptation_score
            self.weight_carried = total_weight
        else:
            self.adaptation_score = 0
            self.weight_carried = 0
            adaptation_score = 0

        return adaptation_score

    def mutate(self):
        self.chromosomes = [
            not chromosome
            if random.random() < self.MUTATION_PROBABILITY
            else chromosome
            for chromosome in self.chromosomes
        ]

    def crossover(self, other_parent, double_point_crossover_enabled: bool):
        if double_point_crossover_enabled:
            self.__double_point_crossover(other_parent)
        else:
            self.__single_point_crossover(other_parent)

    def get_adaptation_score(self) -> int:
        return self.adaptation_score

    def __calculate_weight_and_adaptation(
        self, backpack_entries: list[DataEntry]
    ) -> (int, int):
        total_weight = 0
        adaptation_score = 0
        for i in range(0, self.chromosomes_count):
            if self.chromosomes[i]:
                adaptation_score += backpack_entries[i].value
                total_weight += backpack_entries[i].weight

        return total_weight, adaptation_score

    def __are_backpack_entries_valid(self, backpack_entries: list[DataEntry]):
        return len(backpack_entries) == self.chromosomes_count

    def __single_point_crossover(self, other_parent):
        crossover_point = self.__generate_crossover_point()

        self.chromosomes = (
            self.chromosomes[0:crossover_point]
            + other_parent.chromosomes[crossover_point:]
        )

    def __double_point_crossover(self, other_parent):
        first_crossover_point = self.__generate_crossover_point()
        second_crossover_point = first_crossover_point

        while second_crossover_point == first_crossover_point:
            second_crossover_point = self.__generate_crossover_point()

        (
            first_crossover_point,
            second_crossover_point,
        ) = self.__get_sorted_crossover_points(
            first_crossover_point, second_crossover_point
        )

        self.chromosomes = (
            self.chromosomes[0:first_crossover_point]
            + other_parent.chromosomes[first_crossover_point:second_crossover_point]
            + self.chromosomes[second_crossover_point:]
        )

    # python list operator does not include upper bound of the range, safe to use full length
    def __generate_crossover_point(self) -> int:
        return random.randint(0, self.chromosomes_count)

    def __get_sorted_crossover_points(
        self, first_crossover_point: int, second_crossover_point: int
    ) -> (int, int):
        if first_crossover_point > second_crossover_point:
            swap_tmp = first_crossover_point
            first_crossover_point = second_crossover_point
            second_crossover_point = swap_tmp

        return first_crossover_point, second_crossover_point

    def __str__(self) -> int:
        return f"{self.adaptation_score} | {self.chromosomes}"

    def __repr__(self) -> int:
        return str(self)

    @staticmethod
    def generate_random(entries_count: int):
        generated_chromosomes: list[bool] = []
        for i in range(0, entries_count):
            generated_chromosomes.append(bool(random.getrandbits(1)))

        return Candidate(generated_chromosomes)
