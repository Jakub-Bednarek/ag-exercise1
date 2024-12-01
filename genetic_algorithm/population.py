class Candidate:
    def __init__(self):
        self.chromosomes: Array[Boolean] = []
        self.solution_score: int = 0

    def calculate_solution_score(self):
        pass

    def set_chromosome(self, index: int, value: Boolean):
        pass


class Population:
    def __init__(self, population_size: int, adaptation_function):
        self.candidates: Array[Candidate] = self.generate_random_population(
            population_size
        )
        self.adaptation_function = None

    def generate_random_population(self, population_size: int) -> Array[Candidate]:
        pass

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


def simulate_population(iterations_count: int):
    population = Population(0, None)
    simulation_results: Array[int] = []

    n_steps_simulated = 0
    while n_steps_simulated < iterations_count:
        population.run_simulation_step()
        simulation_results.append(population.find_best_candidate())

    return simulation_results
