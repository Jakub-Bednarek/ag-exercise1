#!/bin/python3

from helpers.data_loader import load_data, InvalidInputFilePathException

def main():
    print("Hello there")

    loaded_data = None
    try:
        loaded_data = load_data("./data/low-dimensional/file.txt")
    except Exception as e:
        print(e)
        return 1

    print(loaded_data.objects_count)
    print(loaded_data.storage_size)
    print(len(loaded_data.data_set))


if __name__ == "__main__":
    main()
