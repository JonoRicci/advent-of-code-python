"""
Day 1

"""

import sys
import os
from typing import List, Tuple
from collections import Counter

# Add jono_aoc_helpers (local pip module)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from jono_aoc_helpers.logger import initiate_logging
from jono_aoc_helpers.arguments import get_arguments
from jono_aoc_helpers.request_input import get_puzzle_input
from jono_aoc_helpers.timing import timed
from jono_aoc_helpers import load_input

YEAR = 2024  # YYYY
DAY = 1  # D

# Set up helpers
args = get_arguments()
logger = initiate_logging(args.level)


def main() -> None:
    """
    Call helpers to carry out routine tasks.
    Then call solution functions.
    """
    # Request input from AoC via curl
    get_puzzle_input(YEAR, DAY)

    # Load puzzle input via the helper module
    puzzle_input = load_input.load_puzzle_input_as_string(YEAR, DAY)

    # Calculate results and log it
    try:
        part_1_result = part_1(puzzle_input)
        logger.info(f"Part 1: {part_1_result}")
    except Exception as e:
        logger.error(f"Error during Part 1: {e}")

    try:
        part_2_result = part_2(puzzle_input)
        logger.info(f"Part 2: {part_2_result}")
    except Exception as e:
        logger.error(f"Error during Part 2: {e}")


@timed()
def part_1(puzzle_input: str) -> int:
    """
    Calculate the total distance between paired numbers.

    :param puzzle_input: The two lists of numbers
    """
    left_list, right_list = parse_input(puzzle_input)

    left_list.sort()
    right_list.sort()
    total_distance: int = 0

    logger.debug(f"Sorted Left List: {left_list}")
    logger.debug(f"Sorted Right List: {right_list}")

    for left, right in zip(left_list, right_list):
        distance = abs(left - right)
        logger.debug(f"Pair ({left}, {right}), Distance: {distance}")
        total_distance += distance

    return total_distance


def parse_input(puzzle_input: str) -> Tuple[List[int], List[int]]:
    """
    Parse the puzzle input into two lists.

    :param puzzle_input: The two lists of numbers
    """
    left_list: List[int] = []
    right_list: List[int] = []

    for line in puzzle_input.strip().split("\n"):
        try:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
        except ValueError:
            logger.error(f"Invalid line in input: {line}")
            raise ValueError(f"Input parsing failed for line: {line}")

    logger.debug(f"Left list: {left_list}")
    logger.debug(f"Right list: {right_list}")

    return left_list, right_list


@timed()
def part_2(puzzle_input: str) -> int:
    """
    Calculate the similarity score between the two lists.

    :param puzzle_input: The two lsits of numbers
    """
    left_list, right_list = parse_input(puzzle_input)

    # Count occurrences in the right list with builtin Counter
    right_count = Counter(right_list)
    logger.debug(right_count)

    total_similarity_score: int = 0

    for left in left_list:
        count = right_count[left]  # Get count of left number from right list
        similarity_score = left * count
        logger.debug(
            f"Number: {left}, Right apperances: {count}, similarity score: {similarity_score}"
        )
        total_similarity_score += similarity_score

    return total_similarity_score


if __name__ == "__main__":
    main()
