"""
Day 05

"""

from collections import defaultdict
from typing import Tuple
from logger import logger


def main() -> None:
    """
    Import the puzzle input, process and display the results.

    """
    puzzle_input = import_list()
    logger.debug(puzzle_input)

    hv_overlap, diagonal_overlap = hydrothermal_venture(puzzle_input)
    logger.info(
        f"Part 01: There are {hv_overlap} points where two lines "
        f"overlap considering only horizontal and vertical lines."
    )
    logger.info(
        f"Part 02: There are {diagonal_overlap} points where two "
        f"lines overlap considering diagonal lines included."
    )


def import_list() -> list:
    """
    Import the puzzle input and return a list.

    :return: Puzzle input text file as list
    :rtype: list
    """
    file = open("puzzle-input", "r")
    string_list = file.read().splitlines()
    file.close()
    return string_list


def hydrothermal_venture(vent_coordinates: list) -> Tuple[int, int]:
    """
    Extract coordinates as integers from input list.
    Get the direction of each line (positive / negative).
    For each value in the largest direction:
        Record each coordinate point of the line.
        Add to either part1 or/and part2 dict.
        If the coordinate already exists in the dict, += 1 to it's key.
    Calculate overlap by extracting from dicts length of all keys over 1.
    """
    # Key:
    part_01 = defaultdict(int)
    part_02 = defaultdict(int)

    for line in vent_coordinates:
        logger.debug(line)
        start, end = line.split("->")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")

        x1 = int(x1.strip())
        y1 = int(y1.strip())
        x2 = int(x2.strip())
        y2 = int(y2.strip())

        x_direction = x2 - x1
        y_direction = y2 - y1

        logger.debug(f"X direction: {x_direction}, Y direction: {y_direction}")
        logger.debug(range(1 + max(abs(x_direction), abs(y_direction))))

        for i in range(1 + max(abs(x_direction), abs(y_direction))):
            x = x1 + (1 if x_direction > 0 else (-1 if x_direction < 0 else 0)) * i
            y = y1 + (1 if y_direction > 0 else (-1 if y_direction < 0 else 0)) * i

            # For horizontal and vertical only
            if x_direction == 0 or y_direction == 0:
                part_01[(x, y)] += 1

            # For diagonals
            part_02[(x, y)] += 1

    horizontal_vertical_overlap = len([k for k in part_01 if part_01[k] > 1])
    diagonal_overlap = len([k for k in part_02 if part_02[k] > 1])

    return horizontal_vertical_overlap, diagonal_overlap


if __name__ == "__main__":
    main()
