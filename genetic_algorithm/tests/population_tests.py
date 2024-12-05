import unittest

from unittest.mock import Mock, ANY, patch
from genetic_algorithm.population import Population, PopulationConfig

EXPECTED_ADAPTATION_SCORE = 55
EXPECTED_CANDIDATES_SIZE = 5


def create_candidate_mock(adaptation_score):
    mock = Mock()
    mock.crossover = Mock()
    mock.mutate = Mock()
    mock.get_adaptation_score = Mock(return_value=adaptation_score)
    mock.calculate_adaptation_score = Mock()

    return mock


def create_candidate_mock_list():
    return [
        create_candidate_mock(13),
        create_candidate_mock(8),
        create_candidate_mock(55),
        create_candidate_mock(0),
        create_candidate_mock(25),
    ]


def create_selection_function_mock(candidates_list):
    mock = Mock()
    mock.select = Mock(return_value=candidates_list)

    return mock


def create_population_config(adaptation_function, double_point_crossover_enabled):
    return PopulationConfig(
        population_size=EXPECTED_CANDIDATES_SIZE,
        adaptation_function=adaptation_function,
        entries_count=1,
        backpack_limit=0,
        backpack_entries=[],
        double_point_crossover_enabled=double_point_crossover_enabled,
    )


class TestPopulation(unittest.TestCase):
    def test_should_generate_corrent_number_of_candidates(self):
        population_config = create_population_config(None, False)

        sut = Population(population_config)

        self.assertEqual(len(sut.candidates), EXPECTED_CANDIDATES_SIZE)

    def test_should_calculate_adaptation_scores_and_get_best_candidate(self):
        candidates_list = create_candidate_mock_list()
        selection_function = create_selection_function_mock(candidates_list)
        population_config = create_population_config(selection_function, False)

        sut = Population(population_config)
        sut.candidates = candidates_list

        self.assertEqual(sut.run_calculation_step(), EXPECTED_ADAPTATION_SCORE)

        candidates_list[0].calculate_adaptation_score.assert_called_once()
        self.assertEqual(candidates_list[0].get_adaptation_score.call_count, 2)

        candidates_list[1].calculate_adaptation_score.assert_called_once()
        candidates_list[1].get_adaptation_score.assert_called_once()

        candidates_list[2].calculate_adaptation_score.assert_called_once()
        self.assertEqual(candidates_list[2].get_adaptation_score.call_count, 2)

        candidates_list[3].calculate_adaptation_score.assert_called_once()
        candidates_list[3].get_adaptation_score.assert_called_once()

        candidates_list[4].calculate_adaptation_score.assert_called_once()
        candidates_list[4].get_adaptation_score.assert_called_once()

    def test_should_do_single_point_crossover_and_mutation_for_each_candidate(self):
        candidates_list = create_candidate_mock_list()
        selection_function = create_selection_function_mock(candidates_list)
        population_config = create_population_config(selection_function, False)

        sut = Population(population_config)
        sut.candidates = candidates_list

        random_mock = Mock(return_value=0.0)
        with patch("random.random", random_mock):
            sut.run_genetic_modification_step()

        candidates_list[0].crossover.assert_called_once_with(ANY, False)
        candidates_list[1].crossover.assert_called_once_with(ANY, False)
        candidates_list[2].crossover.assert_called_once_with(ANY, False)
        candidates_list[3].crossover.assert_called_once_with(ANY, False)
        candidates_list[4].crossover.assert_called_once_with(ANY, False)

        candidates_list[0].mutate.assert_called_once()
        candidates_list[1].mutate.assert_called_once()
        candidates_list[2].mutate.assert_called_once()
        candidates_list[3].mutate.assert_called_once()
        candidates_list[4].mutate.assert_called_once()

    def test_should_do_double_point_crossover_and_mutation_for_each_candidate(self):
        candidates_list = create_candidate_mock_list()
        selection_function = create_selection_function_mock(candidates_list)
        population_config = create_population_config(selection_function, True)

        sut = Population(population_config)
        sut.candidates = candidates_list

        random_mock = Mock(return_value=0.0)
        with patch("random.random", random_mock):
            sut.run_genetic_modification_step()

        candidates_list[0].crossover.assert_called_once_with(ANY, True)
        candidates_list[1].crossover.assert_called_once_with(ANY, True)
        candidates_list[2].crossover.assert_called_once_with(ANY, True)
        candidates_list[3].crossover.assert_called_once_with(ANY, True)
        candidates_list[4].crossover.assert_called_once_with(ANY, True)

        candidates_list[0].mutate.assert_called_once()
        candidates_list[1].mutate.assert_called_once()
        candidates_list[2].mutate.assert_called_once()
        candidates_list[3].mutate.assert_called_once()
        candidates_list[4].mutate.assert_called_once()

    def test_should_do_only_mutation_for_each_candidate(self):
        candidates_list = create_candidate_mock_list()
        selection_function = create_selection_function_mock(candidates_list)
        population_config = create_population_config(selection_function, True)

        sut = Population(population_config)
        sut.candidates = candidates_list

        random_mock = Mock(return_value=1.0)
        with patch("random.random", random_mock):
            sut.run_genetic_modification_step()

        candidates_list[0].mutate.assert_called_once()
        candidates_list[1].mutate.assert_called_once()
        candidates_list[2].mutate.assert_called_once()
        candidates_list[3].mutate.assert_called_once()
        candidates_list[4].mutate.assert_called_once()
