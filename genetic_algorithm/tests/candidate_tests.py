import unittest

from unittest.mock import Mock, patch
from genetic_algorithm.helpers.data_loader import DataEntry
from genetic_algorithm.candidate import Candidate, InvalidBackpackEntriesSizeException

DUMMY_BACKPACK_VALUES = [
    DataEntry(10, 20),
    DataEntry(15, 2),
    DataEntry(1, 3),
    DataEntry(5, 8),
    DataEntry(20, 5),
]

LOW_BACKPACK_STORAGE_SIZE = 10
HIGH_BACKPACK_STORAGE_SIZE = 40
DEFAULT_MUTATION_PROBABILITY = 0.1


def always_zero_random():
    return 0.0


def always_one_random():
    return 1.0


def lower_bound_randint(x, y):
    return 0


def upper_bound_randint(x, y):
    return 4


def one_point_crossover_randint(x, y):
    return 2


class TestCandidate(unittest.TestCase):
    def test_candidate_should_return_valid_adaptation_score(self):
        expected_adaptation_score = 51
        test_candidate = Candidate([1, 1, 1, 1, 1], DEFAULT_MUTATION_PROBABILITY)

        test_candidate.calculate_adaptation_score(
            DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
        )

        self.assertEqual(
            test_candidate.get_adaptation_score(), expected_adaptation_score
        )

    def test_candidate_should_return_zero_adaptation_score(self):
        expected_adaptation_score = 0
        test_candidate = Candidate([1, 1, 1, 1, 1], DEFAULT_MUTATION_PROBABILITY)

        test_candidate.calculate_adaptation_score(
            DUMMY_BACKPACK_VALUES, LOW_BACKPACK_STORAGE_SIZE
        )

        self.assertEqual(
            test_candidate.get_adaptation_score(), expected_adaptation_score
        )

    def test_candidate_should_raise_when_backpack_entries_size_does_not_match_chromosomes_size(
        self,
    ):
        test_candidate = Candidate([1, 1, 1, 1, 1, 1], DEFAULT_MUTATION_PROBABILITY)

        with self.assertRaises(InvalidBackpackEntriesSizeException):
            test_candidate.calculate_adaptation_score(
                DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
            )

    @patch("random.random", always_zero_random)
    def test_candidate_should_mutate_all_chromosomes(self):
        pre_mutation_adaptation_score = 51
        post_mutation_adaptation_score = 0
        test_candidate = Candidate([1, 1, 1, 1, 1], DEFAULT_MUTATION_PROBABILITY)

        self.assertEqual(
            test_candidate.calculate_adaptation_score(
                DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
            ),
            pre_mutation_adaptation_score,
        )

        test_candidate.mutate()

        self.assertEqual(
            test_candidate.calculate_adaptation_score(
                DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
            ),
            post_mutation_adaptation_score,
        )

    @patch("random.random", always_one_random)
    def test_candidate_should_not_mutate_any_chromosome(self):
        expected_adaptation_score = 51
        test_candidate = Candidate([1, 1, 1, 1, 1], DEFAULT_MUTATION_PROBABILITY)

        self.assertEqual(
            test_candidate.calculate_adaptation_score(
                DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
            ),
            expected_adaptation_score,
        )

        test_candidate.mutate()

        self.assertEqual(
            test_candidate.calculate_adaptation_score(
                DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
            ),
            expected_adaptation_score,
        )

    @patch("random.randint", one_point_crossover_randint)
    def test_candidate_should_perform_single_point_crossover_with_index_in_the_middle(
        self,
    ):
        pre_crossover_adaptation_score = 46
        post_crossover_adaptation_score = 30
        first_crossover_parent = Candidate(
            [1, 1, 1, 0, 1], DEFAULT_MUTATION_PROBABILITY
        )
        second_crossover_parent = Candidate(
            [0, 1, 0, 1, 0], DEFAULT_MUTATION_PROBABILITY
        )

        self.assertEqual(
            first_crossover_parent.calculate_adaptation_score(
                DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
            ),
            pre_crossover_adaptation_score,
        )

        first_crossover_parent.crossover(
            second_crossover_parent, double_point_crossover_enabled=False
        )

        self.assertEqual(
            first_crossover_parent.calculate_adaptation_score(
                DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
            ),
            post_crossover_adaptation_score,
        )

    @patch("random.randint", lower_bound_randint)
    def test_candidate_should_perform_single_point_crossover_with_index_at_the_start(
        self,
    ):
        pre_crossover_adaptation_score = 46
        post_crossover_adaptation_score = 20
        first_crossover_parent = Candidate(
            [1, 1, 1, 0, 1], DEFAULT_MUTATION_PROBABILITY
        )
        second_crossover_parent = Candidate(
            [0, 1, 0, 1, 0], DEFAULT_MUTATION_PROBABILITY
        )

        self.assertEqual(
            first_crossover_parent.calculate_adaptation_score(
                DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
            ),
            pre_crossover_adaptation_score,
        )

        first_crossover_parent.crossover(
            second_crossover_parent, double_point_crossover_enabled=False
        )

        self.assertEqual(
            first_crossover_parent.calculate_adaptation_score(
                DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
            ),
            post_crossover_adaptation_score,
        )

    @patch("random.randint", upper_bound_randint)
    def test_candidate_should_perform_single_point_crossover_with_index_at_the_end(
        self,
    ):
        pre_crossover_adaptation_score = 46
        post_crossover_adaptation_score = 26
        first_crossover_parent = Candidate(
            [1, 1, 1, 0, 1], DEFAULT_MUTATION_PROBABILITY
        )
        second_crossover_parent = Candidate(
            [0, 1, 0, 1, 0], DEFAULT_MUTATION_PROBABILITY
        )

        self.assertEqual(
            first_crossover_parent.calculate_adaptation_score(
                DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
            ),
            pre_crossover_adaptation_score,
        )

        first_crossover_parent.crossover(
            second_crossover_parent, double_point_crossover_enabled=False
        )

        self.assertEqual(
            first_crossover_parent.calculate_adaptation_score(
                DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
            ),
            post_crossover_adaptation_score,
        )

    def test_candidate_should_perform_double_point_crossover_with_index_in_the_middle(
        self,
    ):
        randint_mock = Mock(side_effect=[2, 4])

        pre_crossover_adaptation_score = 46
        post_crossover_adaptation_score = 50
        first_crossover_parent = Candidate(
            [1, 1, 1, 0, 1], DEFAULT_MUTATION_PROBABILITY
        )
        second_crossover_parent = Candidate(
            [0, 1, 0, 1, 0], DEFAULT_MUTATION_PROBABILITY
        )

        with patch("random.randint", randint_mock):
            self.assertEqual(
                first_crossover_parent.calculate_adaptation_score(
                    DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
                ),
                pre_crossover_adaptation_score,
            )

            first_crossover_parent.crossover(
                second_crossover_parent, double_point_crossover_enabled=True
            )

            self.assertEqual(
                first_crossover_parent.calculate_adaptation_score(
                    DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
                ),
                post_crossover_adaptation_score,
            )

    def test_candidate_should_perform_double_point_crossover_with_index_covering_whole_range(
        self,
    ):
        pre_crossover_adaptation_score = 46
        post_crossover_adaptation_score = 20
        first_crossover_parent = Candidate(
            [1, 1, 1, 0, 1], DEFAULT_MUTATION_PROBABILITY
        )
        second_crossover_parent = Candidate(
            [0, 1, 0, 1, 0], DEFAULT_MUTATION_PROBABILITY
        )

        randint_mock = Mock(side_effect=[0, 5])
        with patch("random.randint", randint_mock):
            self.assertEqual(
                first_crossover_parent.calculate_adaptation_score(
                    DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
                ),
                pre_crossover_adaptation_score,
            )

            first_crossover_parent.crossover(
                second_crossover_parent, double_point_crossover_enabled=True
            )
            print(first_crossover_parent.chromosomes)

            self.assertEqual(
                first_crossover_parent.calculate_adaptation_score(
                    DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
                ),
                post_crossover_adaptation_score,
            )

    def test_candidate_should_perform_double_point_crossover_including_lower_bound_of_range(
        self,
    ):
        pre_crossover_adaptation_score = 46
        post_crossover_adaptation_score = 20
        first_crossover_parent = Candidate(
            [1, 1, 1, 0, 1], DEFAULT_MUTATION_PROBABILITY
        )
        second_crossover_parent = Candidate(
            [0, 1, 0, 1, 0], DEFAULT_MUTATION_PROBABILITY
        )

        randint_mock = Mock(side_effect=[0, 3])
        with patch("random.randint", randint_mock):
            self.assertEqual(
                first_crossover_parent.calculate_adaptation_score(
                    DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
                ),
                pre_crossover_adaptation_score,
            )

            first_crossover_parent.crossover(
                second_crossover_parent, double_point_crossover_enabled=False
            )

            self.assertEqual(
                first_crossover_parent.calculate_adaptation_score(
                    DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
                ),
                post_crossover_adaptation_score,
            )

    def test_candidate_should_perform_double_point_crossover_including_upper_bound_of_range(
        self,
    ):
        pre_crossover_adaptation_score = 46
        post_crossover_adaptation_score = 26
        first_crossover_parent = Candidate(
            [1, 1, 1, 0, 1], DEFAULT_MUTATION_PROBABILITY
        )
        second_crossover_parent = Candidate(
            [0, 1, 0, 1, 0], DEFAULT_MUTATION_PROBABILITY
        )

        randint_mock = Mock(side_effect=[4, 5])
        with patch("random.randint", randint_mock):
            self.assertEqual(
                first_crossover_parent.calculate_adaptation_score(
                    DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
                ),
                pre_crossover_adaptation_score,
            )

            first_crossover_parent.crossover(
                second_crossover_parent, double_point_crossover_enabled=False
            )

            self.assertEqual(
                first_crossover_parent.calculate_adaptation_score(
                    DUMMY_BACKPACK_VALUES, HIGH_BACKPACK_STORAGE_SIZE
                ),
                post_crossover_adaptation_score,
            )
