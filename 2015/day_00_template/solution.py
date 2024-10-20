"""
Day 00

"""

# Add jono_aoc_helpers (local pip module)
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from jono_aoc_helpers import logger
from jono_aoc_helpers import arguments


def main() -> None:
    """
    Call helpers to carry out routine tasks.
    Then call solution functions.
    """
    # Set up helpers
    args = arguments.get_arguments()
    logs = logger.initiate_logging(args.level)

    # Request input from AoC via curl
    request_input.get_puzzle_input(2015, 00, logs)


if __name__ == "__main__":
    main()
