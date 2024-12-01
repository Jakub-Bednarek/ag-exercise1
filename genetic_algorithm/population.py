import random


class Candidate:
    def __init__(self, chromosomes: list[bool]):
        self.chromosomes: list[bool] = chromosomes
        self.solution_score: int = 0

    def calculate_solution_score(self):
        pass

    def set_chromosome(self, index: int, value: bool):
        pass

    @staticmethod
    def generate_random(problem_size: int):
        generated_chromosomes: list[bool] = []
        for i in range(0, problem_size):
            generated_chromosomes.append(bool(random.getrandbits(1)))

        return Candidate(generated_chromosomes)

    def __str__(self):
        return f"{self.solution_score} | {self.chromosomes}"

    def __repr__(self):
        return str(self)


class Population:
    CROSS_PROBABILITY = 0.5
    MUTATION_PROBABILITY = 0.1

    def __init__(self, population_size: int, adaptation_function, problem_size: int):
        self.adaptation_function = None
        self.problem_size = problem_size
        self.candidates: list[Candidate] = self.generate_random_population(
            population_size
        )

    def generate_random_population(self, population_size: int) -> list[Candidate]:
        generated_population: list[Candidate] = []
        for i in range(0, population_size):
            candidate = Candidate.generate_random(self.problem_size)
            generated_population.append(candidate)

        return generated_population

    def run_simulation_step(self) -> int:
        return 0

    def find_best_cadidate(self) -> int:
        return 0

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


def simulate_population(iterations_count: int):
    population = Population(0, None)
    simulation_results: list[int] = []

    n_steps_simulated = 0
    while n_steps_simulated < iterations_count:
        population.run_simulation_step()
        simulation_results.append(population.find_best_candidate())

    return simulation_results
