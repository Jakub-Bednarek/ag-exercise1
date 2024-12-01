#!/bin/python3

from helpers.data_loader import load_data, InvalidInputFilePathException
from helpers.script_args import parse_script_args
from genetic_algorithm.population import Candidate, Population


def main():
    parsed_args = parse_script_args()

    loaded_data = None
    try:
        loaded_data = load_data(parsed_args.input)
    except Exception as e:
        print(e)
        return 1

    print(loaded_data.objects_count)
    print(loaded_data.storage_size)
    print(len(loaded_data.data_set))

    cand = Candidate.generate_random(10)
    print(cand)

    print("")
    pop = Population(10, None, 15)
    print(pop)


if __name__ == "__main__":
    main()
