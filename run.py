#!/bin/python3

from genetic_algorithm.helpers.data_loader import load_data
from genetic_algorithm.helpers.script_args import parse_script_args
from genetic_algorithm.population import (
    Candidate,
    Population,
    PopulationConfig,
    simulate_population,
)
from example.exercise_2_example import run_all_simulations


def run_example_simulation():
    run_all_simulations()


def run_normal_simulation(parsed_args):
    loaded_data = None
    try:
        loaded_data = load_data(parsed_args.input)
    except Exception as e:
        print(e)
        return 1

    print(loaded_data.backpack_entries_count)
    print(loaded_data.storage_size)
    print(len(loaded_data.backpack_entries))

    its = 1
    for i in range(0, its):
        simulation_results = simulate_population(
            PopulationConfig.create(parsed_args, loaded_data), 10
        )

    print(sorted(simulation_results, reverse=True)[0])


def main():
    parsed_args = parse_script_args()

    if parsed_args.run_example:
        run_example_simulation()
    else:
        run_normal_simulation(parsed_args)


if __name__ == "__main__":
    main()
