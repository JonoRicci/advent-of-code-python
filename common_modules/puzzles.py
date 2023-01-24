"""

"""
import subprocess
from os import getenv
from os.path import exists

# Find SESSION via Firefox:
# 1. Navigate to https://adventofcode.com/2022/day/1/input
# 2. From Developer tools navigate to Network
# 3. Grab the "session" cookie.
# 4. Export as environment variable
SESSION: str = getenv("AOC_SESSION", None)


def import_puzzle(year: int, day: int) -> list:
    """
    Import the puzzle input and return a list.

    :return: Puzzle input text file
    :rtype: list
    """
    puzzle_exists = exists("./puzzle-input.txt")

    if puzzle_exists:
        return read_file()
    else:
        puzzle_input = get_puzzle_input(year, day)
        write_file(puzzle_input)
        return read_file()


def read_file() -> list:
    """
    Import the puzzle input and return a list.

    :return: Puzzle input text file
    :rtype: list
    """
    with open("puzzle-input.txt", "r") as file:
        string_list = file.read().splitlines()
        return string_list


def get_puzzle_input(year: int, day: int) -> str:
    """
    Creates command using the passed in arguments, calls it via subprocess module and returns the output.

    :param year: Year puzzle was released
    :param day: Day puzzle was released
    :return output: Puzzle input from advent of code
    :rtype: str
    """
    if SESSION is None:
        exit(1)
    else:
        command = f'curl https://adventofcode.com/{year}/day/{day}/input --cookie "session={SESSION}"'
        puzzle_input = subprocess.check_output(command, shell=True)
        puzzle_input = puzzle_input.decode("utf-8")
        return puzzle_input


def write_file(puzzle_input: str) -> None:
    """
    Take the puzzle input and write it to a file.

    :param puzzle_input: Puzzle input from advent of code
    """
    with open("puzzle-input.txt", "w") as file:
        file.write(puzzle_input)
