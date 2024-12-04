import random


# TODO: ex_2 MUTATION_PROBABILITY should be config param
class Candidate:
    MUTATION_PROBABILITY = 0.1

    def __init__(self, chromosomes: list[bool]):
        self.chromosomes: list[bool] = chromosomes
        self.chromosomes_count: int = len(self.chromosomes)
        self.adaptation_score: int = 0
        self.weight_carried: int = 0

    def calculate_adaptation_score(self, backpack_entries, backpack_limit):
        adaptation_score = 0
        weight_carried = 0
        for i in range(0, self.chromosomes_count):
            if self.chromosomes[i]:
                adaptation_score += backpack_entries[i].value
                weight_carried += backpack_entries[i].weight

        if not weight_carried > backpack_limit:
            self.adaptation_score = adaptation_score
            self.weight_carried = weight_carried
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

    def crossover(self, other_parent, double_point_crossover_enabled):
        if double_point_crossover_enabled:
            self.__double_point_crossover(other_parent)
        else:
            self.__single_point_crossover(other_parent)

    def get_adaptation_score(self):
        return self.adaptation_score

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

        if first_crossover_point > second_crossover_point:
            swap_tmp = first_crossover_point
            first_crossover_point = second_crossover_point
            second_crossover_point = swap_tmp

        self.chromosomes = (
            self.chromosomes[0:first_crossover_point]
            + other_parent.chromosomes[first_crossover_point:second_crossover_point]
            + self.chromosomes[second_crossover_point:]
        )

    def __generate_crossover_point(self):
        return random.randint(0, self.chromosomes_count - 1)

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
