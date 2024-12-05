from argparse import ArgumentParser
from genetic_algorithm.selection_functions import SelectionFunctionType


def parse_script_args():
    parser = ArgumentParser()

    subparsers = parser.add_subparsers(dest="command")
    example_parser = subparsers.add_parser(
        "run_example", help="Run example simulations"
    )

    normal_subparser = subparsers.add_parser(
        "run_normal", help="Fully customizable run"
    )
    normal_subparser.add_argument(
        "-i",
        "--input",
        type=str,
        help="Path to file with the data. Path can be relative or absolute",
        required=True,
    )
    normal_subparser.add_argument(
        "-s",
        "--population-size",
        type=int,
        help="Size of the population for algorithm evaluation",
        default=10,
    )
    normal_subparser.add_argument(
        "-n",
        "--iterations",
        type=int,
        help="Number of iterations to be executed for selected algorithm",
        default=100,
    )
    normal_subparser.add_argument(
        "-a",
        "--selection-function",
        choices=SelectionFunctionType.__members__,
        help="Selection function to be executed in the algorithm",
        default=SelectionFunctionType.ROULETTE,
    )
    normal_subparser.add_argument(
        "-c",
        "--crossover-probability",
        type=int,
        help="Chance for crossover to occur for each candidate during genetic modification simulation step",
        default=0.5,
    )
    normal_subparser.add_argument(
        "-m",
        "--mutation-probability",
        type=float,
        help="Chance for mutation to occur for each gene in candidate during genetic modification simulation step",
        default=0.1,
    )
    normal_subparser.add_argument(
        "-d",
        "--double-point-crossover",
        help="Enable double point crossover for genetic functions",
        default=False,
        action="store_true",
    )

    return parser.parse_args()
