"""
Get Advent of Code Puzzle Input.
"""

# !/usr/bin/python3
import argparse
import os
import subprocess

# Find SESSION via Firefox:
# 1. Navigate to https://adventofcode.com/2022/day/1/input
# 2. From Developer tools navigate to Network
# 3. Grab the "session" cookie.
# 4. Export as environment variable
SESSION: str = os.getenv("AOC_SESSION", "")


def main() -> None:
    """
    Gather command line arguments, request puzzle input and print to file.
    """
    arguments: argparse.Namespace = get_arguments()
    puzzle_input = get_puzzle_input(arguments)
    write_file(puzzle_input)


def write_file(puzzle_input: str) -> None:
    """
    Take the puzzle input and write it to a file.

    :param puzzle_input: Puzzle input from advent of code
    """
    with open("puzzle-input.txt", "w") as file:
        file.write(puzzle_input)


def get_puzzle_input(arguments: argparse.Namespace) -> str:
    """
    Creates command using the passed in arguments, calls it via subprocess module and returns the output.

    :param arguments: Command line arguments
    :return output: Puzzle input from advent of code
    :rtype: str
    """
    command = f'curl https://adventofcode.com/{arguments.year}/day/{arguments.day}/input --cookie "session={SESSION}"'
    puzzle_input = subprocess.check_output(command, shell=True)
    puzzle_input = puzzle_input.decode("utf-8")
    return puzzle_input


def get_arguments() -> argparse.Namespace:
    """
    Grab command line arguments and return.

    :return: Arguments object
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description="Read input")
    parser.add_argument("--year", type=int, default=2022)
    parser.add_argument("--day", type=int, default=1)
    return parser.parse_args()


if __name__ == "__main__":
    main()
