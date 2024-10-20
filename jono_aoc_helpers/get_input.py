"""
Get Advent of Code Puzzle Input.
"""

# !/usr/bin/python3
import argparse
import logging
import os
import subprocess

# Find SESSION via Firefox:
# 1. Navigate to https://adventofcode.com/2022/day/1/input
# 2. From Developer tools navigate to Network
# 3. Grab the "session" cookie.
# 4. Export as environment variable
SESSION: str = os.getenv("AOC_SESSION", "")


def get_puzzle_input(year: int, day: int, logger: "logging.Logger") -> None:
    """
    Get puzzle input for the specified year and day, and write it to a file. If the file already exists, do not request the input again to avoid unnecessary requests.

    :param year: Year of the puzzle
    :param day: Day of the puzzle
    :param logger: Logger for logging debug and error messages
    """
    file_name = f"puzzle-input"

    # Define the file path relative to the current directory
    file_name = os.path.join(os.path.dirname(__file__), f"day_{day}", "puzzle-input")

    # Check if the input file already exists
    if os.path.exists(file_name):
        logger.debug(f"Input for {year}, {day} already exists: {file_name}")
        return

    # Create command to fetch the puzzle input
    command = [
        "curl",
        f"https://adventofcode.com/{year}/day/{day}/input",
        "--cookie",
        f"session={SESSION}",
    ]
    try:
        puzzle_input = subprocess.check_output(command)
        puzzle_input = puzzle_input.decode("utf-8")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to fetch input: {e}")
        return

    # Ensure the directory for the day exists
    os.makedirs(os.path.dirname(file_name), exist_ok=True)

    # Write puzzle input to a file
    with open(file_name, "w") as file:
        file.write(puzzle_input)
        logger.debug(
            f"Puzzle input for year {year}, day {day} has been written to {file_name}"
        )
