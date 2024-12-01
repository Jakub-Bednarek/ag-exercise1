#!/bin/python3

from genetic_algorithm.helpers.data_loader import load_data
from genetic_algorithm.helpers.script_args import parse_script_args
from genetic_algorithm.population import (
    Candidate,
    Population,
    PopulationConfig,
    simulate_population,
)


def main():
    parsed_args = parse_script_args()

    loaded_data = None
    try:
        loaded_data = load_data(parsed_args.input)
    except Exception as e:
        print(e)
        return 1

    print(loaded_data.entries_count)
    print(loaded_data.storage_size)
    print(len(loaded_data.backpack_entries))

    for i in range(0, 1000):
        print(i)
        simulation_results = simulate_population(
            PopulationConfig.create(parsed_args, loaded_data), 3
        )
    print(simulation_results)


if __name__ == "__main__":
    main()
