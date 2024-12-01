import random

from dataclasses import dataclass
from genetic_algorithm.helpers.data_loader import ProgramData, DataEntry
from genetic_algorithm.adaptation_functions import (
    AdaptationFunctionFactory,
    AdaptationFunctionBase,
)


class Candidate:
    def __init__(self, chromosomes: list[bool]):
        self.chromosomes: list[bool] = chromosomes
        self.adaptation_score: int = 0

    def calculate_adaptation_score(self, backpack_entries):
        adaptation_score = 0
        for i in range(0, len(self.chromosomes)):
            if self.chromosomes[i]:
                adaptation_score += backpack_entries[i].value

        self.adaptation_score = adaptation_score

        return adaptation_score

    def set_chromosome(self, index: int, value: bool):
        pass

    def is_exceeding_limit(self, backpack_limit):
        return self.adaptation_score <= backpack_limit

    def __str__(self):
        return f"{self.adaptation_score} | {self.chromosomes}"

    def __repr__(self):
        return str(self)

    @staticmethod
    def generate_random(entries_count: int):
        generated_chromosomes: list[bool] = []
        for i in range(0, entries_count):
            generated_chromosomes.append(bool(random.getrandbits(1)))

        return Candidate(generated_chromosomes)


@dataclass
class PopulationConfig:
    population_size: int
    adaptation_function: AdaptationFunctionBase
    entries_count: int
    storage_size: int
    backpack_entries: list[DataEntry]

    @staticmethod
    def create(program_arguments, program_data):
        return PopulationConfig(
            program_arguments.population_size,
            AdaptationFunctionFactory.create(
                type=program_arguments.adaptation_function
            ),
            program_data.entries_count,
            program_data.storage_size,
            program_data.backpack_entries,
        )


class Population:
    CROSS_PROBABILITY = 0.5
    MUTATION_PROBABILITY = 0.1

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
            candidate.calculate_adaptation_score(self.config.backpack_entries)

            if not candidate.is_exceeding_limit(self.config.storage_size) and candidate.adaptation_score > best_candidate_adaptation:
                best_candidate_adaptation = candidate.adaptation_score

        return best_candidate_adaptation

    def run_mutation_step(self):
        pass

    def __cross_candidates(self):
        pass

    def __mutate_candidate(self):
        pass

    def __try_to_apply_genetic_operator(self):
        pass

    def __apply_adapatation_function(self):
        pass

    def __str__(self):
        return "\n".join([str(candidate) for candidate in self.candidates])

    def __repr__(self):
        return str(self)


def simulate_population(population_config: PopulationConfig, iterations: int):
    population = Population(population_config)

    simulation_results: list[int] = []
    n_steps_simulated = 0
    while n_steps_simulated < iterations:
        print(f"\n---------Iteration {n_steps_simulated + 1}---------")
        best_candidate_adaptation = population.run_calculation_step()
        simulation_results.append(best_candidate_adaptation)
        print(population)

        if n_steps_simulated == iterations:
            return simulation_results

        population.run_mutation_step()

        n_steps_simulated += 1

    return simulation_results
