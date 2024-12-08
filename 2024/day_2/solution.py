"""
Day 2

"""

import sys
import os
from typing import List

# Add jono_aoc_helpers (local pip module)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from jono_aoc_helpers.logger import initiate_logging
from jono_aoc_helpers.arguments import get_arguments
from jono_aoc_helpers.request_input import get_puzzle_input
from jono_aoc_helpers.timing import timed
from jono_aoc_helpers import load_input

YEAR = 2024  # YYYY
DAY = 2  # D

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
    puzzle_input = load_input.load_puzzle_input_as_list(YEAR, DAY)

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
def part_1(puzzle_input: List[str]) -> int:
    """
    Count the number of safe reports.

    :param puzzle_input: List of strings, each line representing a report
    :return: Number of safe reports
    """
    safe_count = 0

    for line in puzzle_input:
        try:
            report = list(map(int, line.split()))
            if is_safe(report):
                safe_count += 1
        except ValueError:
            logger.error(f"Invalid report data: {line}")
            raise ValueError(f"Could not parse report: {line}")

    return safe_count


def is_safe(report: List[int]) -> bool:
    """
    Check if a single report is safe.

    :param report: A single report with a list of levels.
    :return: Safety status of report
    """
    # For each report, gather a list of the differences between each adjacent level
    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    logger.debug(f"Differences: {differences}")

    # Check if all differences are increasing or decreasing
    is_increasing = all(1 <= difference <= 3 for difference in differences)
    is_decreasing = all(-3 <= difference <= -1 for difference in differences)

    return is_increasing or is_decreasing


@timed()
def part_2(puzzle_input: List[str]) -> int:
    """
    Count the number of safe reports with the Problem Dampener.

    :param puzzle_input: List of strings, each line representing a report
    :return: Number of safe reports
    """
    safe_count = 0

    for line in puzzle_input:
        try:
            report = list(map(int, line.split()))
            if is_safe_with_dampener(report):
                safe_count += 1
        except ValueError:
            logger.error(f"Invalid report data: {line}")
            raise ValueError(f"Could not parse report: {line}")

    return safe_count


def is_safe_with_dampener(report: List[int]) -> bool:
    """
    Check if a single report is safe considering the problem dampener.

    :param report: A single report with a list of levels.
    :return: Safety status of report
    """
    # Use existing check to avoid unnecessary work
    if is_safe(report):
        return True

    # Check if removing one level makes the report safe
    for i in range(len(report)):
        # Slice a single element from the list (up to index and beyond)
        modified_report = report[:i] + report[i + 1 :]
        if is_safe(modified_report):
            logger.debug(
                f"Report {report} is safe with dampener by removing index {i}: {modified_report}"
            )
            return True

    return False


if __name__ == "__main__":
    main()
