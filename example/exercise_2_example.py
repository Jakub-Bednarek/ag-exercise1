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

SMALL_POPULATION_SIZE = 30
SMALL_POPULATION_ITERATION_COUNT = 1000
LARGE_POPULATION_SIZE = 1000000
LARGE_POPULATION_ITERATION_COUNT = 10
DEFAULT_MUTATION_PROBABILITY = 0.2
DEFAULT_CROSSOVER_PROBABILITY = 0.5

OUTPUT_DIR = "output/"


class PlottableDataset:
    def __init__(self, data, label):
        self.data = data
        self.size = len(self.data)
        self.label = label


def draw_single_simulation_plot(
    simulation_results: list[float], plot_title: str, output_file: str
):
    fig, ax = plt.subplots()
    fig.set_size_inches(18.5, 10.5)
    ax.plot(range(0, len(simulation_results)), simulation_results)

    ax.set_xlabel("Iterations")
    ax.set_ylabel("Adaptation score")
    ax.set_title(plot_title)

    plt.savefig(output_file)
    plt.close()


def draw_single_plot_with_multiple_datasets(
    plottable_datasets: PlottableDataset, plot_title: str, output_file: str
):
    last_data_set_size = plottable_datasets[0].size
    x_axis_values = range(1, last_data_set_size + 1)

    fig, ax = plt.subplots()
    fig.set_size_inches(18.5, 10.5)
    ax.set_xlabel("Iterations")
    ax.set_ylabel("Adaptation score")
    ax.set_title(plot_title)
    for data_set in plottable_datasets:
        if data_set.size != last_data_set_size:
            print(
                f"Error: unepxected data set size: {data_set.size}, expected {last_data_set_size}"
            )
            continue

        last_data_set_size = data_set.size

        ax.plot(x_axis_values, data_set.data, label=data_set.label)

    ax.legend()

    plt.savefig(output_file, dpi=300)
    print(f"\n - Plot file saved to: {output_file}")


def run_simulation(
    population_size: int,
    selection_function_type: SelectionFunctionType,
    input_file: str,
    iterations_count: int,
    mutation_probability: float,
    crossover_probability: float,
    double_point_crossover_enabled: bool = False,
    draw_plot: bool = False,
    plot_title: str = "",
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

    print("\n------Simulation Start------")
    print("\nPopulation config:")
    print(population_config)
    print("\nSimulation config:")
    print(f"\tIterations count: {iterations_count}")
    print("\nRunning:")

    simulation_results = []
    try:
        simulation_results = simulate_population(population_config, iterations_count)
    except Exception as e:
        print(f"Simulation failed: {e}")
        return []

    if draw_plot:
        draw_single_simulation_plot(simulation_results, output_file)

    print("\n------Simulation Finished------")

    return simulation_results


def run_simulation_on_all_test_data_files():
    SMALL_DATA_OUTPUT = "example/output/all_tests/low_dimensional"
    LARGE_DATA_OUTPUT = "example/output/all_tests/high_dimensional"

    if not os.path.exists(SMALL_DATA_OUTPUT):
        os.makedirs(SMALL_DATA_OUTPUT)

    for input_file in SMALL_DATA_FILES:
        output_file_name = os.path.splitext(os.path.basename(input_file))[0] + ".png"

        run_simulation(
            SMALL_POPULATION_SIZE,
            SelectionFunctionType.TOURNAMENT,
            input_file,
            SMALL_POPULATION_ITERATION_COUNT,
            DEFAULT_MUTATION_PROBABILITY,
            DEFAULT_CROSSOVER_PROBABILITY,
            draw_plot=True,
            plot_title=input_file,
            output_file=os.path.join(SMALL_DATA_OUTPUT, output_file_name),
        )

    if not os.path.exists(LARGE_DATA_OUTPUT):
        os.makedirs(LARGE_DATA_OUTPUT)

    for input_file in LARGE_DATA_FILES:
        mutation_probability = random.random()
        crossover_probability = random.random()

        output_file_name = os.path.splitext(os.path.basename(input_file))[0] + ".png"

        run_simulation(
            LARGE_POPULATION_SIZE,
            SelectionFunctionType.TOURNAMENT,
            input_file,
            LARGE_POPULATION_ITERATION_COUNT,
            DEFAULT_MUTATION_PROBABILITY,
            DEFAULT_CROSSOVER_PROBABILITY,
            draw_plot=True,
            plot_title=input_file,
            output_file=os.path.join(LARGE_DATA_OUTPUT, output_file_name),
        )


def run_mutation_and_crossover_simulation():
    simulations_count = 5
    small_data_output = "example/output/mutation_crossover/low_dimensional/"
    large_data_output = "example/output/mutation_crossover/high_dimensional/"
    small_mutation_data_output_file = os.path.join(
        small_data_output, "small_mutation__simulation.png"
    )
    small_crossover_data_output_file = os.path.join(
        small_data_output, "small_crossover_simulation.png"
    )
    large_mutation_data_output_file = os.path.join(
        large_data_output, "large_mutation__simulation.png"
    )
    large_crossover_data_output_file = os.path.join(
        large_data_output, "large_crossover_simulation.png"
    )

    if not os.path.exists(small_data_output):
        os.makedirs(small_data_output)

    if not os.path.exists(large_data_output):
        os.makedirs(large_data_output)

    small_data_mutation_results = []
    mutation_probability = [0.02, 0.04, 0.06, 0.08, 0.1]
    for i in range(0, simulations_count):
        result = run_simulation(
            SMALL_POPULATION_SIZE,
            SelectionFunctionType.ROULETTE,
            SMALL_DATA_FILE_4,
            SMALL_POPULATION_ITERATION_COUNT,
            mutation_probability[i],
            DEFAULT_CROSSOVER_PROBABILITY,
            draw_plot=False,
        )

        small_data_mutation_results.append(
            PlottableDataset(
                result, f"m_{mutation_probability}_c_{crossover_probability}"
            )
        )

    draw_single_plot_with_multiple_datasets(
        small_data_mutation_results,
        "Mutation impact on small data set",
        small_mutation_data_output_file,
    )

    large_data_mutation_results = []
    for i in range(0, simulations_count):
        result = run_simulation(
            LARGE_POPULATION_SIZE,
            SelectionFunctionType.ROULETTE,
            LARGE_DATA_FILE_2,
            LARGE_POPULATION_ITERATION_COUNT,
            mutation_probability[i],
            DEFAULT_CROSSOVER_PROBABILITY,
            draw_plot=False,
        )

        large_data_mutation_results.append(
            PlottableDataset(result, f"mutation_{mutation_probability[i]}")
        )

    draw_single_plot_with_multiple_datasets(
        large_data_mutation_results,
        "Mutation impact on small data set",
        large_mutation_data_output_file,
    )

    crossover_probability = [0.02, 0.04, 0.06, 0.08, 0.1]
    small_data_crossover_results = []
    mutation_probability = [0.02, 0.04, 0.06, 0.08, 0.1]
    for i in range(0, simulations_count):
        result = run_simulation(
            SMALL_POPULATION_SIZE,
            SelectionFunctionType.ROULETTE,
            SMALL_DATA_FILE_4,
            SMALL_POPULATION_ITERATION_COUNT,
            DEFAULT_MUTATION_PROBABILITY,
            crossover_probability[i],
            draw_plot=False,
        )

        small_data_crossover_results.append(
            PlottableDataset(result, f"crossover_{crossover_probability[i]}")
        )

    draw_single_plot_with_multiple_datasets(
        small_data_crossover_results,
        "Mutation impact on small data set",
        small_crossover_data_output_file,
    )

    large_data_crossover_results = []
    for i in range(0, simulations_count):
        result = run_simulation(
            LARGE_POPULATION_SIZE,
            SelectionFunctionType.ROULETTE,
            LARGE_DATA_FILE_2,
            LARGE_POPULATION_ITERATION_COUNT,
            DEFAULT_MUTATION_PROBABILITY,
            crossover_probability[i],
            draw_plot=False,
        )

        large_data_crossover_results.append(
            PlottableDataset(result, f"crossover_{crossover_probability[i]}")
        )

    draw_single_plot_with_multiple_datasets(
        large_data_crossover_results,
        "Mutation impact on small data set",
        large_crossover_data_output_file,
    )


def run_rank_and_roulette_simulation():
    simulations_results = []
    data_output_path = "example/output/rank_and_roulette/"
    data_output_file = os.path.join(data_output_path, "rank_and_roulette.png")

    if not os.path.exists(data_output_path):
        os.makedirs(data_output_path)

    result = run_simulation(
        SMALL_POPULATION_SIZE,
        SelectionFunctionType.RANK,
        SMALL_DATA_FILE_1,
        SMALL_POPULATION_ITERATION_COUNT,
        DEFAULT_MUTATION_PROBABILITY,
        DEFAULT_CROSSOVER_PROBABILITY,
        draw_plot=False,
        output_file=data_output_file,
    )

    simulations_results.append(PlottableDataset(result, f"rank_selection"))

    result = run_simulation(
        SMALL_POPULATION_SIZE,
        SelectionFunctionType.ROULETTE,
        SMALL_DATA_FILE_1,
        SMALL_POPULATION_ITERATION_COUNT,
        DEFAULT_MUTATION_PROBABILITY,
        DEFAULT_CROSSOVER_PROBABILITY,
        draw_plot=False,
        output_file=data_output_file,
    )

    simulations_results.append(PlottableDataset(result, f"roulette_selection"))

    draw_single_plot_with_multiple_datasets(
        simulations_results, "Rank vs roulette selection comparison", data_output_file
    )


def run_single_and_double_point_crossover_simulation():
    simulations_results = []
    data_output_path = "example/output/mutation_crossover/"
    data_output_file = os.path.join(
        data_output_path, "mutation_crossover_simulation.png"
    )

    if not os.path.exists(data_output_path):
        os.makedirs(data_output_path)

    result = run_simulation(
        SMALL_POPULATION_SIZE,
        SelectionFunctionType.TOURNAMENT,
        SMALL_DATA_FILE_1,
        SMALL_POPULATION_ITERATION_COUNT,
        DEFAULT_MUTATION_PROBABILITY,
        DEFAULT_CROSSOVER_PROBABILITY,
        draw_plot=False,
    )

    simulations_results.append(PlottableDataset(result, f"single_point_crossover"))

    result = run_simulation(
        SMALL_POPULATION_SIZE,
        SelectionFunctionType.TOURNAMENT,
        SMALL_DATA_FILE_1,
        SMALL_POPULATION_ITERATION_COUNT,
        DEFAULT_MUTATION_PROBABILITY,
        DEFAULT_CROSSOVER_PROBABILITY,
        double_point_crossover_enabled=True,
        draw_plot=False,
    )

    simulations_results.append(PlottableDataset(result, f"double_point_crossover"))

    draw_single_plot_with_multiple_datasets(
        simulations_results, "Single vs double crossover comparison", data_output_file
    )


def run_rank_roulette_and_tournament_simulation():
    simulations_results = []
    data_output_path = "example/output/rank_roulette_tournament/"
    data_output_file = os.path.join(
        data_output_path, "rank_roulette_tournament_simulation.png"
    )

    if not os.path.exists(data_output_path):
        os.makedirs(data_output_path)

    result = run_simulation(
        SMALL_POPULATION_SIZE,
        SelectionFunctionType.TOURNAMENT,
        SMALL_DATA_FILE_1,
        SMALL_POPULATION_ITERATION_COUNT,
        DEFAULT_MUTATION_PROBABILITY,
        DEFAULT_CROSSOVER_PROBABILITY,
        draw_plot=False,
    )

    simulations_results.append(PlottableDataset(result, f"tournament_selection"))

    result = run_simulation(
        SMALL_POPULATION_SIZE,
        SelectionFunctionType.ROULETTE,
        SMALL_DATA_FILE_1,
        SMALL_POPULATION_ITERATION_COUNT,
        DEFAULT_MUTATION_PROBABILITY,
        DEFAULT_CROSSOVER_PROBABILITY,
        draw_plot=False,
    )

    simulations_results.append(PlottableDataset(result, f"roulette_selection"))

    result = run_simulation(
        SMALL_POPULATION_SIZE,
        SelectionFunctionType.RANK,
        SMALL_DATA_FILE_1,
        SMALL_POPULATION_ITERATION_COUNT,
        DEFAULT_MUTATION_PROBABILITY,
        DEFAULT_CROSSOVER_PROBABILITY,
        draw_plot=False,
    )

    simulations_results.append(PlottableDataset(result, f"rank_selection"))

    draw_single_plot_with_multiple_datasets(
        simulations_results,
        "Rank vs roulette vs tournament selection comparison",
        data_output_file,
    )


def run_all_simulations():
    # run_simulation_on_all_test_data_files()
    # run_mutation_and_crossover_simulation()
    run_rank_and_roulette_simulation()
    run_single_and_double_point_crossover_simulation()
    run_rank_roulette_and_tournament_simulation()
