from argparse import ArgumentParser
from genetic_algorithm.adaptation_functions import AdaptationFunctionType


def parse_script_args():
    parser = ArgumentParser()

    parser.add_argument(
        "-i",
        "--input",
        type=str,
        help="Path to file with the data. Path can be relative or absolute",
        required=True,
    )
    parser.add_argument(
        "-s",
        "--population-size",
        type=int,
        help="Size of the population for algorithm evaluation",
        default=10,
    )
    parser.add_argument(
        "-n",
        "--iterations",
        type=int,
        help="Number of iterations to be executed for selected algorithm",
        default=100,
    )
    parser.add_argument(
        "-a",
        "--adaptation-function",
        choices=AdaptationFunctionType,
        help="Adapation function to be executed in the algorithm",
        default=0,
    )
    parser.add_argument(
        "-f",
        "--selection-function",
        type=int,
        help="Selection function to be executed in the algorithm",
        default=0,
    )
    parser.add_argument(
        "-c",
        "--cross-function",
        type=int,
        help="Cross function to be executed in the algorithm",
        default=0,
    )
    parser.add_argument(
        "-m",
        "--mutation-function",
        type=int,
        help="Mutation function to be executed in the algorithm",
        default=0,
    )

    return parser.parse_args()
