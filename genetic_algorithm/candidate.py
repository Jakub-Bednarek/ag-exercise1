import random


class Candidate:
    MUTATION_PROBABILITY = 0.1

    def __init__(self, chromosomes: list[bool]):
        self.chromosomes: list[bool] = chromosomes
        self.adaptation_score: int = 0
        self.weight_carried: int = 0

    def calculate_adaptation_score(self, backpack_entries, backpack_limit):
        adaptation_score = 0
        weight_carried = 0
        for i in range(0, len(self.chromosomes)):
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

    def set_chromosome(self, index: int, value: bool):
        pass

    def mutate(self):
        self.chromosomes = [
            not chromosome
            if random.random() < self.MUTATION_PROBABILITY
            else chromosome
            for chromosome in self.chromosomes
        ]

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
