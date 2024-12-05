import random

from dataclasses import dataclass
from genetic_algorithm.helpers.data_loader import ProgramData, DataEntry
from genetic_algorithm.selection_functions import (
    SelectionFunctionFactory,
    SelectionFunctionBase,
)
from genetic_algorithm.candidate import Candidate


@dataclass
class PopulationConfig:
    population_size: int
    selection_function: SelectionFunctionBase
    entries_count: int
    backpack_limit: int
    backpack_entries: list[DataEntry]
    double_point_crossover_enabled: bool

    @staticmethod
    def create(program_arguments, program_data):
        return PopulationConfig(
            program_arguments.population_size,
            SelectionFunctionFactory.create(
                function_type=program_arguments.selection_function
            ),
            program_data.entries_count,
            program_data.storage_size,
            program_data.backpack_entries,
            program_arguments.double_point_crossover,
        )


# TODO: ex_2 CROSS_PROBABILITY should be config param
class Population:
    CROSS_PROBABILITY = 0.5

    def __init__(self, config: PopulationConfig):
        self.config = config
        self.candidates: list[Candidate] = self.generate_random()

    def generate_random(self) -> list[Candidate]:
        generated_population: list[Candidate] = []
        for i in range(0, self.config.population_size):
            candidate = Candidate.generate_random(self.config.entries_count)
            generated_population.append(candidate)

        return generated_population

    def run_calculation_step(self) -> int:
        best_candidate_adaptation = 0

        for candidate in self.candidates:
            candidate.calculate_adaptation_score(
                self.config.backpack_entries, self.config.backpack_limit
            )

            if candidate.get_adaptation_score() > best_candidate_adaptation:
                best_candidate_adaptation = candidate.get_adaptation_score()

        return best_candidate_adaptation

    def run_genetic_modification_step(self):
        new_population = self.__select_new_candidates()
        self.__apply_genetic_operators_on_population(new_population)

        self.candidates = new_population

    def __apply_genetic_operators_on_population(self, candidates: list[Candidate]):
        self.__apply_genetic_crossover(candidates)
        self.__apply_genetic_mutation(candidates)

    def __apply_genetic_crossover(self, candidates: list[Candidate]):
        for i in range(0, len(self.candidates)):
            if random.random() > self.CROSS_PROBABILITY:
                continue

            other_parent_index = i
            while other_parent_index == i:
                other_parent_index = random.randint(0, self.config.population_size - 1)

            candidates[i].crossover(
                candidates[other_parent_index],
                self.config.double_point_crossover_enabled,
            )

    def __apply_genetic_mutation(self, candidates: list[Candidate]):
        for candidate in candidates:
            candidate.mutate()

    def __select_new_candidates(self) -> str:
        return self.config.selection_function.select(self.candidates)

    def __str__(self) -> str:
        return "\n".join([str(candidate) for candidate in self.candidates])

    def __repr__(self) -> str:
        return str(self)


def simulate_population(
    population_config: PopulationConfig, iterations: int
) -> list[int]:
    population = Population(population_config)

    simulation_results: list[int] = []
    n_steps_simulated = 0
    while n_steps_simulated < iterations:
        best_candidate_adaptation = population.run_calculation_step()
        simulation_results.append(best_candidate_adaptation)

        if n_steps_simulated == iterations:
            return simulation_results

        population.run_genetic_modification_step()

        n_steps_simulated += 1

    return simulation_results
