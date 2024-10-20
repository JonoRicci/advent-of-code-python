"""
Day 00

"""

from common_modules import logger
from common_modules import arguments
from common_modules import puzzles


def main() -> None:
    """
    Call common modules to carry out routine tasks.
    Then call solution functions.
    """
    # Set up common modules
    args = arguments.get_arguments()
    logs = logger.initiate_logging(args.level)

    puzzle_input = puzzles.import_puzzle(2022, 1)
    logs.debug(puzzle_input)


if __name__ == "__main__":
    main()
