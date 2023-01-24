"""
Get Advent of Code Puzzle Input.
"""

# !/usr/bin/python3
import argparse
import subprocess

# Find SESSION via Firefox:
# 1. Navigate to https://adventofcode.com/2022/day/1/input
# 2. From Developer tools navigate to Network
# 3. Grab the "session" cookie.
SESSION: str = ""


def main() -> None:
    """
    x
    """
    arguments: argparse.Namespace = get_arguments()
    output = get_output(arguments)
    put_output(arguments, output)


def put_output(arguments: argparse.Namespace, output: str) -> None:
    """
    Take the output and write it to a file.

    :param arguments: Command line arguments
    :param output: Puzzle input from advent of code
    """
    with open(f"day-{arguments.day}-puzzle-input.txt", "w") as file:
        file.write(output)


def get_output(arguments: argparse.Namespace) -> str:
    """
    Creates command using the passed in arguments, calls it via subprocess module and returns the output.

    :param arguments: Command line arguments
    :return output: Puzzle input from advent of code
    :rtype: str
    """
    command = f'curl https://adventofcode.com/{arguments.year}/day/{arguments.day}/input --cookie "session={SESSION}"'
    output = subprocess.check_output(command, shell=True)
    output = output.decode("utf-8")
    return output


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
