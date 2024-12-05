import random
import os
import matplotlib.pyplot as plt


from genetic_algorithm.selection_functions import (
    SelectionFunctionType,
    SelectionFunctionFactory,
)
from genetic_algorithm.population import simulate_population, PopulationConfig
from genetic_algorithm.helpers.data_loader import ProgramData, load_data

DATA_PATH = r"data/"
SMALL_DATA_PATH = os.path.join(DATA_PATH, r"low_dimensional")

SMALL_DATA_FILE_0 = os.path.join(SMALL_DATA_PATH, r"file_1.txt")
SMALL_DATA_FILE_1 = os.path.join(SMALL_DATA_PATH, r"file_2.txt")
SMALL_DATA_FILE_2 = os.path.join(SMALL_DATA_PATH, r"file_3.txt")
SMALL_DATA_FILE_3 = os.path.join(SMALL_DATA_PATH, r"file_4.txt")
SMALL_DATA_FILE_4 = os.path.join(SMALL_DATA_PATH, r"file_5.txt")
SMALL_DATA_FILE_5 = os.path.join(SMALL_DATA_PATH, r"file_6.txt")
SMALL_DATA_FILE_6 = os.path.join(SMALL_DATA_PATH, r"file_7.txt")
SMALL_DATA_FILE_7 = os.path.join(SMALL_DATA_PATH, r"file_8.txt")
SMALL_DATA_FILE_8 = os.path.join(SMALL_DATA_PATH, r"file_9.txt")
SMALL_DATA_FILE_9 = os.path.join(SMALL_DATA_PATH, r"file_10.txt")

SMALL_DATA_FILES = [
    SMALL_DATA_FILE_0,
    SMALL_DATA_FILE_1,
    SMALL_DATA_FILE_2,
    SMALL_DATA_FILE_3,
    SMALL_DATA_FILE_4,
    SMALL_DATA_FILE_5,
    SMALL_DATA_FILE_6,
    SMALL_DATA_FILE_7,
    SMALL_DATA_FILE_8,
    SMALL_DATA_FILE_9,
]

LARGE_DATA_PATH = os.path.join(DATA_PATH, r"large_scale")

LARGE_DATA_FILE_0 = os.path.join(LARGE_DATA_PATH, r"file_1.txt")
LARGE_DATA_FILE_1 = os.path.join(LARGE_DATA_PATH, r"file_2.txt")
LARGE_DATA_FILE_2 = os.path.join(LARGE_DATA_PATH, r"file_3.txt")
LARGE_DATA_FILE_3 = os.path.join(LARGE_DATA_PATH, r"file_4.txt")
LARGE_DATA_FILE_4 = os.path.join(LARGE_DATA_PATH, r"file_5.txt")
LARGE_DATA_FILE_5 = os.path.join(LARGE_DATA_PATH, r"file_6.txt")
LARGE_DATA_FILE_6 = os.path.join(LARGE_DATA_PATH, r"file_7.txt")
LARGE_DATA_FILE_7 = os.path.join(LARGE_DATA_PATH, r"file_8.txt")
LARGE_DATA_FILE_8 = os.path.join(LARGE_DATA_PATH, r"file_9.txt")
LARGE_DATA_FILE_9 = os.path.join(LARGE_DATA_PATH, r"file_10.txt")
LARGE_DATA_FILE_10 = os.path.join(LARGE_DATA_PATH, r"file_11.txt")
LARGE_DATA_FILE_11 = os.path.join(LARGE_DATA_PATH, r"file_12.txt")

LARGE_DATA_FILES = [
    LARGE_DATA_FILE_0,
    LARGE_DATA_FILE_1,
    LARGE_DATA_FILE_2,
    LARGE_DATA_FILE_3,
    LARGE_DATA_FILE_4,
    LARGE_DATA_FILE_5,
    LARGE_DATA_FILE_6,
    LARGE_DATA_FILE_7,
    LARGE_DATA_FILE_8,
    LARGE_DATA_FILE_9,
    LARGE_DATA_FILE_10,
    LARGE_DATA_FILE_11,
]

DEFAULT_POPULATION_SIZE = 1000
DEFAULT_SIMULATION_ITERATIONS = 1000

OUTPUT_DIR = "output/"


def draw_single_simulation_plot(simulation_results, output_file):
    fig, ax = plt.subplots()
    ax.plot(range(0, len(simulation_results)), simulation_results)

    plt.savefig(output_file)
    plt.close()


def run_simulation(
    population_size: int,
    selection_function_type: SelectionFunctionType,
    input_file: str,
    iterations_count: int,
    mutation_probability: float,
    crossover_probability: float,
    draw_plot=False,
    output_file="",
):
    try:
        program_data = load_data(input_file)
    except Exception as e:
        print(e)
        return []

    population_config = PopulationConfig(
        population_size,
        SelectionFunctionFactory.create(selection_function_type),
        program_data.backpack_entries_count,
        program_data.storage_size,
        program_data.backpack_entries,
        False,
        mutation_probability,
        crossover_probability,
    )

    print("------Starting simulation------")

    try:
        simulation_results = simulate_population(population_config, iterations_count)
    except Exception as e:
        print(f"Simulation failed: {e}")
        return []

    if draw_plot:
        draw_single_simulation_plot(simulation_results, output_file)

    return simulation_results


def run_simulation_on_all_test_data_files():
    SMALL_DATA_OUTPUT = "example/output/all_tests/low_dimensional"
    LARGE_DATA_OUTPUT = "example/output/all_test/high_dimensional"

    if not os.path.exists(SMALL_DATA_OUTPUT):
        os.makedirs(SMALL_DATA_OUTPUT)

    for input_file in SMALL_DATA_FILES:
        mutation_probability = random.random()
        crossover_probability = random.random()

        output_file_name = os.path.splitext(os.path.basename(input_file))[0] + ".png"

        run_simulation(
            10,
            SelectionFunctionType.TOURNAMENT,
            input_file,
            100,
            mutation_probability,
            crossover_probability,
            True,
            os.path.join(SMALL_DATA_OUTPUT, output_file_name),
        )

    if not os.path.exists(LARGE_DATA_OUTPUT):
        os.makedirs(LARGE_DATA_OUTPUT)

    for input_file in LARGE_DATA_FILES:
        mutation_probability = random.random()
        crossover_probability = random.random()

        output_file_name = os.path.splitext(os.path.basename(input_file))[0] + ".png"

        run_simulation(
            10,
            SelectionFunctionType.TOURNAMENT,
            input_file,
            100,
            mutation_probability,
            crossover_probability,
            True,
            os.path.join(LARGE_DATA_OUTPUT, output_file_name),
        )


def run_mutation_and_crossover_simulation():
    pass


def run_rank_and_roulette_simulation():
    pass


def run_single_and_double_point_crossover_simulation():
    pass


def run_rank_roulette_and_tournament_simulation():
    pass


def run_all_simulations():
    run_simulation_on_all_test_data_files()
    run_mutation_and_crossover_simulation()
    run_rank_and_roulette_simulation()
    run_single_and_double_point_crossover_simulation()
    run_rank_roulette_and_tournament_simulation()
