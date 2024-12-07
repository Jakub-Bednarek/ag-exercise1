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
    backpack_entries_count: int
    backpack_limit: int
    backpack_entries: list[DataEntry]
    double_point_crossover_enabled: bool
    mutation_probability: float
    crossover_probability: float

    @staticmethod
    def create(program_arguments, program_data):
        return PopulationConfig(
            program_arguments.population_size,
            SelectionFunctionFactory.create(
                function_type=program_arguments.selection_function
            ),
            program_data.backpack_entries_count,
            program_data.storage_size,
            program_data.backpack_entries,
            program_arguments.double_point_crossover,
            program_arguments.mutation_probability,
            program_arguments.crossover_probability,
        )

    def __str__(self) -> str:
        return f"\tPopulation size: {self.population_size}\n\tSelection function: {self.selection_function}\n\tBackpack entries size: {self.backpack_entries_count}\n\tBackpack limit: {self.backpack_limit}\n\tDouble point crossover enabled: {self.double_point_crossover_enabled}\n\tMutation probability: {self.mutation_probability}\n\tCrossover probability: {self.crossover_probability}"


class Population:
    def __init__(self, config: PopulationConfig):
        self.config = config
        self.candidates: list[Candidate] = self.generate_random()

    def generate_random(self) -> list[Candidate]:
        generated_population: list[Candidate] = []
        for i in range(0, self.config.population_size):
            candidate = Candidate.generate_random(
                self.config.backpack_entries_count, self.config.mutation_probability
            )
            generated_population.append(candidate)

        return generated_population

    def run_calculation_step(self) -> float:
        best_candidate_adaptation = 0.0

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
        for i in range(0, self.config.population_size):
            if random.random() > self.config.crossover_probability:
                continue

            other_parent_index = i
            while other_parent_index == i:
                other_parent_index = random.randint(0, self.config.population_size - 1)

            candidates.append(
                candidates[i].crossover(
                    candidates[other_parent_index],
                    self.config.double_point_crossover_enabled,
                )
            )

    def __apply_genetic_mutation(self, candidates: list[Candidate]):
        for candidate in candidates:
            candidate.mutate()

    def __select_new_candidates(self) -> list[Candidate]:
        return self.config.selection_function.select(
            self.candidates, self.config.population_size
        )

    def __str__(self) -> str:
        return "\n".join([str(candidate) for candidate in self.candidates])

    def __repr__(self) -> str:
        return str(self)


def simulate_population(
    population_config: PopulationConfig, iterations: int
) -> list[float]:
    population = Population(population_config)

    status_checkpoint = float(iterations) / 10
    next_status_checkpoint = status_checkpoint
    checkpoints_reached = 0

    simulation_results: list[float] = []
    n_steps_simulated = 0
    while n_steps_simulated < iterations:
        best_candidate_adaptation = population.run_calculation_step()
        simulation_results.append(best_candidate_adaptation)

        if n_steps_simulated == iterations:
            return simulation_results

        population.run_genetic_modification_step()

        n_steps_simulated += 1

        if n_steps_simulated > next_status_checkpoint:
            checkpoints_reached += 1
            next_status_checkpoint = checkpoints_reached * status_checkpoint

            print(f"\t{checkpoints_reached * 10}%...")

    return simulation_results
