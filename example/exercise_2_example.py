import random
import os
import matplotlib.pyplot as plt


from genetic_algorithm.selection_functions import (
    SelectionFunctionType,
    SelectionFunctionFactory,
)
from genetic_algorithm.population import simulate_population, PopulationConfig
from genetic_algorithm.helpers.data_loader import ProgramData, load_data, load_optimum

DATA_PATH = r"data/"
SMALL_DATA_PATH = os.path.join(DATA_PATH, r"low_dimensional")

SMALL_DATA_FILE_1 = os.path.join(SMALL_DATA_PATH, r"file_1.txt")
SMALL_DATA_FILE_2 = os.path.join(SMALL_DATA_PATH, r"file_2.txt")
SMALL_DATA_FILE_3 = os.path.join(SMALL_DATA_PATH, r"file_3.txt")
SMALL_DATA_FILE_4 = os.path.join(SMALL_DATA_PATH, r"file_4.txt")
SMALL_DATA_FILE_5 = os.path.join(SMALL_DATA_PATH, r"file_5.txt")
SMALL_DATA_FILE_6 = os.path.join(SMALL_DATA_PATH, r"file_6.txt")
SMALL_DATA_FILE_7 = os.path.join(SMALL_DATA_PATH, r"file_7.txt")
SMALL_DATA_FILE_8 = os.path.join(SMALL_DATA_PATH, r"file_8.txt")
SMALL_DATA_FILE_9 = os.path.join(SMALL_DATA_PATH, r"file_9.txt")
SMALL_DATA_FILE_10 = os.path.join(SMALL_DATA_PATH, r"file_10.txt")

SMALL_DATA_OPTIMUM_PATH = os.path.join(DATA_PATH, r"low_dimensional_optimum")

SMALL_DATA_FILE_OPTIMUM_1 = os.path.join(SMALL_DATA_OPTIMUM_PATH, r"file_1.txt")
SMALL_DATA_FILE_OPTIMUM_2 = os.path.join(SMALL_DATA_OPTIMUM_PATH, r"file_2.txt")
SMALL_DATA_FILE_OPTIMUM_3 = os.path.join(SMALL_DATA_OPTIMUM_PATH, r"file_3.txt")
SMALL_DATA_FILE_OPTIMUM_4 = os.path.join(SMALL_DATA_OPTIMUM_PATH, r"file_4.txt")

SMALL_DATA_FILES = [
    SMALL_DATA_FILE_1,
    SMALL_DATA_FILE_2,
    SMALL_DATA_FILE_3,
    SMALL_DATA_FILE_4,
    SMALL_DATA_FILE_5,
    SMALL_DATA_FILE_6,
    SMALL_DATA_FILE_7,
    SMALL_DATA_FILE_8,
    SMALL_DATA_FILE_9,
    SMALL_DATA_FILE_10,
]

LARGE_DATA_PATH = os.path.join(DATA_PATH, r"large_scale")

LARGE_DATA_FILE_1 = os.path.join(LARGE_DATA_PATH, r"file_1.txt")
LARGE_DATA_FILE_2 = os.path.join(LARGE_DATA_PATH, r"file_2.txt")
LARGE_DATA_FILE_3 = os.path.join(LARGE_DATA_PATH, r"file_3.txt")
LARGE_DATA_FILE_4 = os.path.join(LARGE_DATA_PATH, r"file_4.txt")
LARGE_DATA_FILE_5 = os.path.join(LARGE_DATA_PATH, r"file_5.txt")
LARGE_DATA_FILE_6 = os.path.join(LARGE_DATA_PATH, r"file_6.txt")
LARGE_DATA_FILE_7 = os.path.join(LARGE_DATA_PATH, r"file_7.txt")
LARGE_DATA_FILE_8 = os.path.join(LARGE_DATA_PATH, r"file_8.txt")
LARGE_DATA_FILE_9 = os.path.join(LARGE_DATA_PATH, r"file_9.txt")
LARGE_DATA_FILE_10 = os.path.join(LARGE_DATA_PATH, r"file_10.txt")
LARGE_DATA_FILE_11 = os.path.join(LARGE_DATA_PATH, r"file_11.txt")
LARGE_DATA_FILE_12 = os.path.join(LARGE_DATA_PATH, r"file_12.txt")

LARGE_DATA_OPTIMUM_PATH = os.path.join(DATA_PATH, r"large_scale_optimum")

LARGE_DATA_OPTIMUM_FILE_5 = os.path.join(LARGE_DATA_OPTIMUM_PATH, r"file_5.txt")
LARGE_DATA_OPTIMUM_FILE_9 = os.path.join(LARGE_DATA_OPTIMUM_PATH, r"file_9.txt")

LARGE_DATA_FILES = [
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
    LARGE_DATA_FILE_12,
]

SMALL_POPULATION_SIZE = 30
SMALL_POPULATION_ITERATION_COUNT = 100
LARGE_POPULATION_SIZE = 10000
LARGE_POPULATION_ITERATION_COUNT = 50
DEFAULT_MUTATION_PROBABILITY = 0.01
DEFAULT_CROSSOVER_PROBABILITY = 0.1

OUTPUT_DIR = "output/"


class PlottableDataset:
    def __init__(self, data, label):
        self.data = data
        self.size = len(self.data)
        self.label = label


def draw_single_simulation_plot(
    simulation_results: list[float],
    plot_title: str,
    output_file: str,
    optimum: int = -1,
):
    fig, ax = plt.subplots()
    fig.set_size_inches(18.5, 10.5)
    ax.plot(range(0, len(simulation_results)), simulation_results)

    if not optimum == -1:
        ax.plot(
            range(0, len(simulation_results)),
            [optimum for i in range(0, len(simulation_results))],
            label="optimum",
        )

    ax.set_xlabel("Iterations")
    ax.set_ylabel("Adaptation score")
    ax.set_title(plot_title)

    plt.savefig(output_file)
    plt.close()


def draw_single_plot_with_multiple_datasets(
    plottable_datasets: PlottableDataset,
    plot_title: str,
    output_file: str,
    optimum: int,
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

    ax.plot(
        x_axis_values, [optimum for i in range(0, len(data_set.data))], label="optimum"
    )
    ax.legend()

    plt.savefig(output_file, dpi=300)
    print(f"\n - Plot file saved to: {output_file}")


def create_if_does_not_exist(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def run_simulation(
    population_size: int,
    selection_function_type: SelectionFunctionType,
    input_file: str,
    optimum_file: str,
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
        optimum = load_optimum(optimum_file)
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
        draw_single_simulation_plot(
            simulation_results, f"{input_file} simulation", output_file, optimum
        )

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
    def run_sim(
        output_dir: str,
        input_files: list[str],
        input_optimum_files: list[str],
        run_type: str,
        mutation_probabilities: list[float] = [],
        crossover_probabilities: list[float] = [],
    ):
        simulations_count = 5
        module_dir = "example/output/mutation_crossover/"
        full_output_dir = os.path.join(
            module_dir,
            f"{'mutation' if mutation_probabilities != [] else 'crossover' }",
            output_dir,
        )

        for file_iteration, file in enumerate(input_files, 0):
            output_file_name = (
                os.path.splitext(os.path.basename(file))[0] + "_results.png"
            )
            full_output_file = os.path.join(full_output_dir, output_file_name)

            create_if_does_not_exist(full_output_dir)

            simulation_results = []
            for i in range(0, simulations_count):
                result = run_simulation(
                    (
                        SMALL_POPULATION_SIZE
                        if run_type == "low_dimensional"
                        else LARGE_POPULATION_SIZE
                    ),
                    SelectionFunctionType.ROULETTE,
                    file,
                    input_optimum_files[file_iteration],
                    (
                        SMALL_POPULATION_ITERATION_COUNT
                        if run_type == "low_dimensional"
                        else LARGE_POPULATION_ITERATION_COUNT
                    ),
                    (
                        mutation_probabilities[i]
                        if mutation_probabilities != []
                        else DEFAULT_MUTATION_PROBABILITY
                    ),
                    (
                        crossover_probabilities[i]
                        if crossover_probabilities != []
                        else DEFAULT_CROSSOVER_PROBABILITY
                    ),
                    draw_plot=False,
                )

                simulation_results.append(
                    PlottableDataset(
                        result,
                        f"{run_type}_{mutation_probabilities[i] if mutation_probabilities != [] else crossover_probabilities[i]}",
                    )
                )

            optimum = load_optimum(input_optimum_files[file_iteration])
            draw_single_plot_with_multiple_datasets(
                simulation_results,
                f"{'Mutation' if mutation_probabilities != [] else 'Crossover'} impact on population",
                full_output_file,
                optimum,
            )

    run_sim(
        "low_dimensional",
        [SMALL_DATA_FILE_1, SMALL_DATA_FILE_2, SMALL_DATA_FILE_3, SMALL_DATA_FILE_4],
        [
            SMALL_DATA_FILE_OPTIMUM_1,
            SMALL_DATA_FILE_OPTIMUM_2,
            SMALL_DATA_FILE_OPTIMUM_3,
            SMALL_DATA_FILE_OPTIMUM_4,
        ],
        "low_dimensional",
        mutation_probabilities=[0.02, 0.04, 0.06, 0.08, 0.1],
    )
    run_sim(
        "high_dimensional",
        [LARGE_DATA_FILE_5, LARGE_DATA_FILE_9],
        [LARGE_DATA_OPTIMUM_FILE_5, LARGE_DATA_OPTIMUM_FILE_9],
        "high_dimensional",
        mutation_probabilities=[0.02, 0.04, 0.06, 0.08, 0.1],
    )
    run_sim(
        "low_dimensional",
        [SMALL_DATA_FILE_1, SMALL_DATA_FILE_2, SMALL_DATA_FILE_3, SMALL_DATA_FILE_4],
        [
            SMALL_DATA_FILE_OPTIMUM_1,
            SMALL_DATA_FILE_OPTIMUM_2,
            SMALL_DATA_FILE_OPTIMUM_3,
            SMALL_DATA_FILE_OPTIMUM_4,
        ],
        "low_dimensional",
        crossover_probabilities=[0.02, 0.04, 0.06, 0.08, 0.1],
    )
    run_sim(
        "high_dimensional",
        [LARGE_DATA_FILE_5, LARGE_DATA_FILE_9],
        [LARGE_DATA_OPTIMUM_FILE_5, LARGE_DATA_OPTIMUM_FILE_9],
        "high_dimensional",
        crossover_probabilities=[0.02, 0.04, 0.06, 0.08, 0.1],
    )


def run_rank_and_roulette_simulation():
    def run_sim(
        output_dir: str,
        input_files: list[str],
        input_optimum_files: list[str],
        run_type: str,
    ):
        module_dir = "example/output/rank_vs_roulette/"
        full_output_dir = os.path.join(module_dir, output_dir)

        for file_iteration, file in enumerate(input_files, 0):
            output_file_name = (
                os.path.splitext(os.path.basename(file))[0] + "_results.png"
            )
            full_output_file = os.path.join(full_output_dir, output_file_name)

            create_if_does_not_exist(full_output_dir)

            simulation_results = []
            result = run_simulation(
                (
                    SMALL_POPULATION_SIZE
                    if run_type == "low_dimensional"
                    else LARGE_POPULATION_SIZE
                ),
                SelectionFunctionType.RANK,
                file,
                input_optimum_files[file_iteration],
                (
                    SMALL_POPULATION_ITERATION_COUNT
                    if run_type == "low_dimensional"
                    else LARGE_POPULATION_ITERATION_COUNT
                ),
                DEFAULT_MUTATION_PROBABILITY,
                DEFAULT_CROSSOVER_PROBABILITY,
                draw_plot=False,
            )

            simulation_results.append(PlottableDataset(result, "rank_selection"))

            result = run_simulation(
                (
                    SMALL_POPULATION_SIZE
                    if run_type == "low_dimensional"
                    else LARGE_POPULATION_SIZE
                ),
                SelectionFunctionType.ROULETTE,
                file,
                input_optimum_files[file_iteration],
                (
                    SMALL_POPULATION_ITERATION_COUNT
                    if run_type == "low_dimensional"
                    else LARGE_POPULATION_ITERATION_COUNT
                ),
                DEFAULT_MUTATION_PROBABILITY,
                DEFAULT_CROSSOVER_PROBABILITY,
                draw_plot=False,
            )

            simulation_results.append(PlottableDataset(result, "roulette_selection"))

            optimum = load_optimum(input_optimum_files[file_iteration])
            draw_single_plot_with_multiple_datasets(
                simulation_results,
                "Rank vs Roulette selection algorithms",
                full_output_file,
                optimum
            )

    run_sim(
        "low_dimensional",
        [SMALL_DATA_FILE_1, SMALL_DATA_FILE_2, SMALL_DATA_FILE_3, SMALL_DATA_FILE_4],
        [
            SMALL_DATA_FILE_OPTIMUM_1,
            SMALL_DATA_FILE_OPTIMUM_2,
            SMALL_DATA_FILE_OPTIMUM_3,
            SMALL_DATA_FILE_OPTIMUM_4,
        ],
        "low_dimensional",
    )
    run_sim(
        "high_dimensional",
        [LARGE_DATA_FILE_5, LARGE_DATA_FILE_9],
        [LARGE_DATA_OPTIMUM_FILE_5, LARGE_DATA_OPTIMUM_FILE_9],
        "high_dimensional",
    )


def run_single_and_double_point_crossover_simulation():
    def run_sim(
        output_dir: str,
        input_files: list[str],
        input_optimum_files: list[str],
        run_type: str,
    ):
        module_dir = "example/output/single_vs_double_point_crossover/"
        full_output_dir = os.path.join(module_dir, output_dir)

        for file_iteration, file in enumerate(input_files, 0):
            output_file_name = (
                os.path.splitext(os.path.basename(file))[0] + "_results.png"
            )
            full_output_file = os.path.join(full_output_dir, output_file_name)

            create_if_does_not_exist(full_output_dir)

            simulation_results = []
            result = run_simulation(
                (
                    SMALL_POPULATION_SIZE
                    if run_type == "low_dimensional"
                    else LARGE_POPULATION_SIZE
                ),
                SelectionFunctionType.ROULETTE,
                file,
                input_optimum_files[file_iteration],
                (
                    SMALL_POPULATION_ITERATION_COUNT
                    if run_type == "low_dimensional"
                    else LARGE_POPULATION_ITERATION_COUNT
                ),
                DEFAULT_MUTATION_PROBABILITY,
                DEFAULT_CROSSOVER_PROBABILITY,
                draw_plot=False,
                double_point_crossover_enabled=False,
            )

            simulation_results.append(
                PlottableDataset(result, "single_point_crossover")
            )

            result = run_simulation(
                (
                    SMALL_POPULATION_SIZE
                    if run_type == "low_dimensional"
                    else LARGE_POPULATION_SIZE
                ),
                SelectionFunctionType.ROULETTE,
                file,
                input_optimum_files[file_iteration],
                (
                    SMALL_POPULATION_ITERATION_COUNT
                    if run_type == "low_dimensional"
                    else LARGE_POPULATION_ITERATION_COUNT
                ),
                DEFAULT_MUTATION_PROBABILITY,
                DEFAULT_CROSSOVER_PROBABILITY,
                draw_plot=False,
                double_point_crossover_enabled=True,
            )

            simulation_results.append(
                PlottableDataset(result, "double_point_crossover")
            )

            optimum = load_optimum(input_optimum_files[file_iteration])
            draw_single_plot_with_multiple_datasets(
                simulation_results,
                "Single vs Double point crossover",
                full_output_file,
                optimum,
            )

    run_sim(
        "low_dimensional",
        [SMALL_DATA_FILE_1, SMALL_DATA_FILE_2, SMALL_DATA_FILE_3, SMALL_DATA_FILE_4],
        [
            SMALL_DATA_FILE_OPTIMUM_1,
            SMALL_DATA_FILE_OPTIMUM_2,
            SMALL_DATA_FILE_OPTIMUM_3,
            SMALL_DATA_FILE_OPTIMUM_4,
        ],
        "low_dimensional",
    )
    run_sim(
        "high_dimensional",
        [LARGE_DATA_FILE_5, LARGE_DATA_FILE_9],
        [LARGE_DATA_OPTIMUM_FILE_5, LARGE_DATA_OPTIMUM_FILE_9],
        "high_dimensional",
    )


def run_rank_roulette_and_tournament_simulation():
    def run_sim(
        output_dir: str,
        input_files: list[str],
        input_optimum_files: list[str],
        run_type: str,
    ):
        module_dir = "example/output/rank_vs_roulette_vs_tournament/"
        full_output_dir = os.path.join(module_dir, output_dir)

        for file_iteration, file in enumerate(input_files, 0):
            output_file_name = (
                os.path.splitext(os.path.basename(file))[0] + "_results.png"
            )
            full_output_file = os.path.join(full_output_dir, output_file_name)

            create_if_does_not_exist(full_output_dir)

            simulation_results = []
            result = run_simulation(
                (
                    SMALL_POPULATION_SIZE
                    if run_type == "low_dimensional"
                    else LARGE_POPULATION_SIZE
                ),
                SelectionFunctionType.RANK,
                file,
                input_optimum_files[file_iteration],
                (
                    SMALL_POPULATION_ITERATION_COUNT
                    if run_type == "low_dimensional"
                    else LARGE_POPULATION_ITERATION_COUNT
                ),
                DEFAULT_MUTATION_PROBABILITY,
                DEFAULT_CROSSOVER_PROBABILITY,
                draw_plot=False,
            )

            simulation_results.append(PlottableDataset(result, "rank_selection"))

            result = run_simulation(
                (
                    SMALL_POPULATION_SIZE
                    if run_type == "low_dimensional"
                    else LARGE_POPULATION_SIZE
                ),
                SelectionFunctionType.ROULETTE,
                file,
                input_optimum_files[file_iteration],
                (
                    SMALL_POPULATION_ITERATION_COUNT
                    if run_type == "low_dimensional"
                    else LARGE_POPULATION_ITERATION_COUNT
                ),
                DEFAULT_MUTATION_PROBABILITY,
                DEFAULT_CROSSOVER_PROBABILITY,
                draw_plot=False,
            )

            simulation_results.append(PlottableDataset(result, "roulette_selection"))

            result = run_simulation(
                (
                    SMALL_POPULATION_SIZE
                    if run_type == "low_dimensional"
                    else LARGE_POPULATION_SIZE
                ),
                SelectionFunctionType.TOURNAMENT,
                file,
                input_optimum_files[file_iteration],
                (
                    SMALL_POPULATION_ITERATION_COUNT
                    if run_type == "low_dimensional"
                    else LARGE_POPULATION_ITERATION_COUNT
                ),
                DEFAULT_MUTATION_PROBABILITY,
                DEFAULT_CROSSOVER_PROBABILITY,
                draw_plot=False,
            )

            simulation_results.append(PlottableDataset(result, "tournament_selection"))

            optimum = load_optimum(input_optimum_files[file_iteration])
            draw_single_plot_with_multiple_datasets(
                simulation_results,
                "Rank vs Roulette vs Tournament selection algorithms",
                full_output_file,
                optimum,
            )

    run_sim(
        "low_dimensional",
        [SMALL_DATA_FILE_1, SMALL_DATA_FILE_2, SMALL_DATA_FILE_3, SMALL_DATA_FILE_4],
        [
            SMALL_DATA_FILE_OPTIMUM_1,
            SMALL_DATA_FILE_OPTIMUM_2,
            SMALL_DATA_FILE_OPTIMUM_3,
            SMALL_DATA_FILE_OPTIMUM_4,
        ],
        "low_dimensional",
    )
    run_sim(
        "high_dimensional",
        [LARGE_DATA_FILE_5, LARGE_DATA_FILE_9],
        [LARGE_DATA_OPTIMUM_FILE_5, LARGE_DATA_OPTIMUM_FILE_9],
        "high_dimensional",
    )


def run_all_simulations():
    # run_simulation_on_all_test_data_files()
    run_mutation_and_crossover_simulation()
    run_rank_and_roulette_simulation()
    run_single_and_double_point_crossover_simulation()
    run_rank_roulette_and_tournament_simulation()
