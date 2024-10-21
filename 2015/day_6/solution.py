"""
Day 06

"""

import sys
import os

# Add jono_aoc_helpers (local pip module)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from jono_aoc_helpers.logger import initiate_logging, LoggerType
from jono_aoc_helpers.arguments import get_arguments
from jono_aoc_helpers.request_input import get_puzzle_input
from jono_aoc_helpers.timing import timed
from jono_aoc_helpers import load_input


def main() -> None:
    """
    Call helpers to carry out routine tasks.
    Then call solution functions.
    """
    # Set up helpers
    args = get_arguments()
    logger = initiate_logging(args.level)

    # Request input from AoC via curl
    get_puzzle_input(2015, 6)

    # Load puzzle input via the helper module
    puzzle_input = load_input.load_puzzle_input_as_list(2015, 6)

    # Calculate results and log it
    part_1_result = part_1(puzzle_input, logger)
    logger.info(f"Part 1: {part_1_result}")
    part_2_result = part_2(puzzle_input, logger)
    logger.info(f"Part 2: {part_2_result}")


@timed()
def part_1(puzzle_input: list, logger: LoggerType) -> int:
    """
    Calculate how many lights are lit after following the instructions.

    :param puzzle_input: List of instructions to apply to the light grid
    :return: Number of lights that are lit
    """
    # Initialise a 1000x1000 grid of lights, all off (False)
    grid = [[False] * 1000 for _ in range(1000)]

    for instruction in puzzle_input:
        # Parse instruction and coordinates
        # logger.debug(instruction)
        parts = instruction.split()
        if parts[0] == "turn":
            action = parts[1]
            start_coords = parts[2]
            end_coords = parts[4]
        elif parts[0] == "toggle":
            action = "toggle"
            start_coords = parts[1]
            end_coords = parts[3]

        start_x, start_y = map(int, start_coords.split(","))
        end_x, end_y = map(int, end_coords.split(","))

        # Apply instruction to the grid
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if action == "on":
                    grid[x][y] = True
                elif action == "off":
                    grid[x][y] = False
                elif action == "toggle":
                    grid[x][y] = not grid[x][y]

    # Count the number of lights that are on
    return sum(row.count(True) for row in grid)


@timed()
def part_2(puzzle_input: list, logger: LoggerType) -> int:
    """
    Calculate the total brightness of all lights after following the instructions.

    :param puzzle_input: List of instructions to apply to the light grid
    :param logger: Logger instance to use for logging messages
    :return: Total brightness of all lights
    """
    # Initialize a 1000x1000 grid of lights, all set to brightness 0
    grid = [[0] * 1000 for _ in range(1000)]

    for instruction in puzzle_input:
        # Parse instruction and coordinates
        parts = instruction.split()
        if parts[0] == "turn":
            action = parts[1]
            start_coords = parts[2]
            end_coords = parts[4]
        elif parts[0] == "toggle":
            action = "toggle"
            start_coords = parts[1]
            end_coords = parts[3]

        start_x, start_y = map(int, start_coords.split(","))
        end_x, end_y = map(int, end_coords.split(","))

        # logger.debug(f"Applying instruction: {instruction}")
        # Apply the instruction to the grid
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                if action == "on":
                    grid[x][y] += 1
                elif action == "off":
                    grid[x][y] = max(0, grid[x][y] - 1)
                elif action == "toggle":
                    grid[x][y] += 2

    # Calculate the total brightness of all lights
    return sum(sum(row) for row in grid)


if __name__ == "__main__":
    main()
