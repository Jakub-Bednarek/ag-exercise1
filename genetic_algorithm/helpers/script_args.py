from argparse import ArgumentParser
from genetic_algorithm.selection_functions import SelectionFunctionType


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
        "--selection-function",
        choices=SelectionFunctionType.__members__,
        help="Selection function to be executed in the algorithm",
        default=SelectionFunctionType.ROULETTE,
    )
    parser.add_argument(
        "-c",
        "--crossover-probability",
        type=int,
        help="Chance for crossover to occur for each candidate during genetic modification simulation step",
        default=0.5,
    )
    parser.add_argument(
        "-m",
        "--mutation-probability",
        type=float,
        help="Chance for mutation to occur for each gene in candidate during genetic modification simulation step",
        default=0.1,
    )
    parser.add_argument(
        "-d",
        "--double-point-crossover",
        help="Enable double point crossover for genetic functions",
        default=False,
        action="store_true",
    )

    return parser.parse_args()
