"""
Day 02

"""

# Add jono_aoc_helpers (local pip module)
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from jono_aoc_helpers.logger import initiate_logging
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
    get_puzzle_input(2015, 2)

    # Load puzzle input via the helper module
    puzzle_input = load_input.load_puzzle_input_as_list(2015, 2)

    # Calculate results and log it
    part_1_result = part_1(puzzle_input)
    logger.info(f"Part 1: {part_1_result}")
    part_2_result = part_2(puzzle_input)
    logger.info(f"Part 2: {part_2_result}")


@timed()
def part_1(puzzle_input: list) -> int:
    """
    Calculate the total amount of wrapping paper required.

    :param puzzle_input: List of dimension strings
    :return: Total square feet of wrapping paper required
    """
    total_paper = 0
    for dimensions in puzzle_input:
        l, w, h = parse_dimensions(dimensions)
        side_areas = [l * w, w * h, h * l]
        surface_area = 2 * (side_areas[0] + side_areas[1] + side_areas[2])
        extra_paper = min(side_areas)
        total_paper += surface_area + extra_paper
    return total_paper


def parse_dimensions(dimensions: str) -> tuple:
    """
    Parse dimensions string into a tuple of integers.

    :param dimensions: Dimension string of the present (e.g. "2x3x4")
    :return: A tuple of (length, width, height)
    """
    l, w, h = map(int, dimensions.split("x"))
    return l, w, h


@timed()
def part_2(puzzle_input: list) -> int:
    """
    Calculate the total amount of ribbon required.

    :param puzzle_input: List of dimension strings
    :return: Total feet of ribbon required
    """
    total_ribbon = 0
    for dimensions in puzzle_input:
        l, w, h = parse_dimensions(dimensions)
        perimeters = [2 * (l + w), 2 * (w + h), 2 * (h + l)]
        smallest_perimeter = min(perimeters)
        volume = l * w * h
        total_ribbon += smallest_perimeter + volume
    return total_ribbon


if __name__ == "__main__":
    main()
