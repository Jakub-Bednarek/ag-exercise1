import unittest

from unittest.mock import Mock, patch

from genetic_algorithm.candidate import Candidate
from genetic_algorithm.adaptation_functions import (
    RouletteSelectionFunction,
    TournamentSelectionFunction,
    RankSelectionFunction,
    EmptyCandidatesListException,
)


def create_candidate_mock(adaptation_score):
    candidate_mock = Mock()
    candidate_mock.get_adaptation_score = Mock(return_value=adaptation_score)

    return candidate_mock


ZERO_SCORE_CANDIDATE = create_candidate_mock(0)
CANDIDATE_0 = create_candidate_mock(55)
CANDIDATE_1 = create_candidate_mock(45)
CANDIDATE_2 = create_candidate_mock(30)
CANDIDATE_3 = create_candidate_mock(10)
CANDIDATE_4 = create_candidate_mock(20)

NON_ZERO_CANDIDATES_LIST = [
    CANDIDATE_0,
    CANDIDATE_1,
    CANDIDATE_2,
    CANDIDATE_3,
    CANDIDATE_4,
]

RANDOM_CANDIDATES_LIST = [
    ZERO_SCORE_CANDIDATE,
    CANDIDATE_2,
    ZERO_SCORE_CANDIDATE,
    ZERO_SCORE_CANDIDATE,
    CANDIDATE_1,
]

EMPTY_TEST_CANDIDATES = []

ZERO_SCORE_TEST_CANDIDATES = [
    ZERO_SCORE_CANDIDATE,
    ZERO_SCORE_CANDIDATE,
    ZERO_SCORE_CANDIDATE,
    ZERO_SCORE_CANDIDATE,
    ZERO_SCORE_CANDIDATE,
]

EXPECTED_CORRECT_OUTPUT_LIST_SIZE = 5


def sorted_choices_result(values, weights, k):
    return [0, 1, 2, 3, 4]


def random_choices_result(values, weights, k):
    return [3, 1, 4, 2, 0]


class TestRouletteSelectionFunction(unittest.TestCase):
    EXPECTED_CANDIDATES_OUTPUT_LIST = [
        CANDIDATE_3,
        CANDIDATE_1,
        CANDIDATE_4,
        CANDIDATE_2,
        CANDIDATE_0,
    ]

    def test_empty_candidates_list(self):
        with self.assertRaises(EmptyCandidatesListException):
            RouletteSelectionFunction().select(EMPTY_TEST_CANDIDATES)

    def test_correct_candidates_list_with_sorted_choices_result(self):
        with patch("random.choices", sorted_choices_result):
            res = RouletteSelectionFunction().select(NON_ZERO_CANDIDATES_LIST.copy())

            self.assertEqual(len(res), EXPECTED_CORRECT_OUTPUT_LIST_SIZE)
            self.assertEqual(res, NON_ZERO_CANDIDATES_LIST)

    def test_correct_candidates_list_with_random_choices_result(self):
        with patch("random.choices", random_choices_result):
            res = RouletteSelectionFunction().select(NON_ZERO_CANDIDATES_LIST.copy())

            self.assertEqual(len(res), EXPECTED_CORRECT_OUTPUT_LIST_SIZE)
            self.assertEqual(res, self.EXPECTED_CANDIDATES_OUTPUT_LIST)

    def test_zero_score_cadidates_list(self):
        res = RouletteSelectionFunction().select(ZERO_SCORE_TEST_CANDIDATES.copy())

        self.assertEqual(len(res), EXPECTED_CORRECT_OUTPUT_LIST_SIZE)
        self.assertEqual(res, ZERO_SCORE_TEST_CANDIDATES)


@staticmethod
def minimum_return_randint(lower_bound, upper_bound):
    return 1


@staticmethod
def maximum_return_randint(lower_bound, upper_bound):
    return 4


@staticmethod
def shuffle_mock(input_list):
    input_list[0] = 3
    input_list[1] = 2
    input_list[2] = 0
    input_list[3] = 4
    input_list[4] = 1


class TestTournamentSelectionFunction(unittest.TestCase):
    EXPECTED_MAXIMUM_SIZE_TOURNAMENT_RESULT_LIST = [
        CANDIDATE_0,
        CANDIDATE_0,
        CANDIDATE_0,
        CANDIDATE_0,
        CANDIDATE_0,
    ]

    EXPECTED_MINIMUM_SIZE_TOURNAMENT_RESULT_LIST = [
        CANDIDATE_3,
        CANDIDATE_3,
        CANDIDATE_3,
        CANDIDATE_3,
        CANDIDATE_3,
    ]

    def test_empty_candidates_list(self):
        with self.assertRaises(EmptyCandidatesListException):
            TournamentSelectionFunction().select(EMPTY_TEST_CANDIDATES)

    @patch("random.randint", minimum_return_randint)
    @patch("random.shuffle", shuffle_mock)
    def test_should_select_the_only_candidate_with_minimum_tournament_size(self):
        res = TournamentSelectionFunction().select(NON_ZERO_CANDIDATES_LIST.copy())

        self.assertEqual(len(res), EXPECTED_CORRECT_OUTPUT_LIST_SIZE)
        self.assertEqual(res, self.EXPECTED_MINIMUM_SIZE_TOURNAMENT_RESULT_LIST)

    @patch("random.randint", maximum_return_randint)
    @patch("random.shuffle", shuffle_mock)
    def test_should_select_best_candidate_with_maximum_tournament_size(self):
        res = TournamentSelectionFunction().select(NON_ZERO_CANDIDATES_LIST.copy())

        self.assertEqual(len(res), EXPECTED_CORRECT_OUTPUT_LIST_SIZE)
        self.assertEqual(res, self.EXPECTED_MAXIMUM_SIZE_TOURNAMENT_RESULT_LIST)

    @patch("random.randint", minimum_return_randint)
    @patch("random.shuffle", shuffle_mock)
    def test_should_select_zero_score_candidate_with_minimum_tournament_size(self):
        res = TournamentSelectionFunction().select(RANDOM_CANDIDATES_LIST.copy())

        self.assertEqual(len(res), EXPECTED_CORRECT_OUTPUT_LIST_SIZE)
        self.assertEqual(
            res[0].get_adaptation_score(), ZERO_SCORE_CANDIDATE.get_adaptation_score()
        )

    def test_zero_score_cadidates_list(self):
        res = TournamentSelectionFunction().select(ZERO_SCORE_TEST_CANDIDATES.copy())

        self.assertEqual(len(res), EXPECTED_CORRECT_OUTPUT_LIST_SIZE)
        self.assertEqual(res, ZERO_SCORE_TEST_CANDIDATES)


class TestRankSelectionFunction(unittest.TestCase):
    EXPECTED_RANDOM_CHOICES_CANDIDATES_LIST = [
        CANDIDATE_4,
        CANDIDATE_1,
        CANDIDATE_3,
        CANDIDATE_2,
        CANDIDATE_0,
    ]

    EXPECTED_SORTED_CHOICES_CANDIDATES_LIST = [
        CANDIDATE_0,
        CANDIDATE_1,
        CANDIDATE_2,
        CANDIDATE_4,
        CANDIDATE_3,
    ]

    def test_empty_candidates_list(self):
        with self.assertRaises(EmptyCandidatesListException):
            RankSelectionFunction().select(EMPTY_TEST_CANDIDATES)

    @patch("random.choices", random_choices_result)
    def test_should_return_candidates_after_correctly_sorting_by_adaptation_score_with_random_choices_result(
        self,
    ):
        res = RankSelectionFunction().select(NON_ZERO_CANDIDATES_LIST.copy())

        self.assertEqual(len(res), EXPECTED_CORRECT_OUTPUT_LIST_SIZE)
        self.assertEqual(res, self.EXPECTED_RANDOM_CHOICES_CANDIDATES_LIST)

    @patch("random.choices", sorted_choices_result)
    def test_should_return_candidates_after_correctly_sorting_by_adaptation_score_with_sorted_choices_result(
        self,
    ):
        res = RankSelectionFunction().select(NON_ZERO_CANDIDATES_LIST.copy())

        self.assertEqual(len(res), EXPECTED_CORRECT_OUTPUT_LIST_SIZE)
        self.assertEqual(res, self.EXPECTED_SORTED_CHOICES_CANDIDATES_LIST)

    def test_sample(self):
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
