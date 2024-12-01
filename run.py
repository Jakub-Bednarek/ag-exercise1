#!/bin/python3

from helpers.data_loader import load_data, InvalidInputFilePathException
from helpers.script_args import parse_script_args


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


if __name__ == "__main__":
    main()
