"""
Day 01

"""

# Add jono_aoc_helpers (local pip module)
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from jono_aoc_helpers import logger
from jono_aoc_helpers import arguments
from jono_aoc_helpers import request_input
from jono_aoc_helpers import load_input


def main() -> None:
    """
    Call helpers to carry out routine tasks.
    Then call solution functions.
    """
    # Set up helpers
    args = arguments.get_arguments()
    logs = logger.initiate_logging(args.level)

    # Request input from AoC via curl
    request_input.get_puzzle_input(2015, 1, logs)

    # Load the puzzle input via the helper module
    instructions = load_input.load_puzzle_input_as_string(2015, 1)

    # Calculate result and log it
    result = calculate_floor(instructions)
    logs.info(f"Santa ends up on floor: {result}")


def calculate_floor(instructions: str) -> int:
    """
    Calculate the resulting floor based on the given instructions.

    :param instructions: String containing the sequence of parentheses
    :return: The floor number that Santa ends up on
    """
    floor = 0
    for char in instructions:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
    return floor


if __name__ == "__main__":
    main()
