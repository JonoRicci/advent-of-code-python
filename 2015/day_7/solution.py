"""
Day 07

"""

import sys
import os
import re

# Add jono_aoc_helpers (local pip module)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from jono_aoc_helpers.logger import initiate_logging
from jono_aoc_helpers.arguments import get_arguments
from jono_aoc_helpers.request_input import get_puzzle_input
from jono_aoc_helpers.timing import timed
from jono_aoc_helpers import load_input

# Set up helpers
args = get_arguments()
logger = initiate_logging(args.level)


def main() -> None:
    """
    Call helpers to carry out routine tasks.
    Then call solution functions.
    """

    # Request input from AoC via curl
    get_puzzle_input(2015, 7)

    # Load puzzle input via the helper module
    puzzle_input = load_input.load_puzzle_input_as_list(2015, 7)

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
def part_1(instructions: list[str]) -> int:
    """
    Evaluates the circuit and returns the signal value for wire 'a'.

    :param instructions: List of instructions to build the circuit
    :return: Value of wire 'a'
    """
    # Parse input into instructions
    instructions_dict = parse_instructions(instructions)

    wires = {}

    return evaluate("a", instructions_dict, wires)


def parse_instructions(instructions: list[str]) -> dict[str, str]:
    """
    Parses the input instructions into a dictionary mapping wire names to their corresponding expression.

    :param instructions: List of strings representing the circuit instructions.
    :return: A dictionary of wire identifiers and their expressions.
    """
    instructions_dict = {}
    for line in instructions:
        # Regex captures two groups, expression on the left and value on the right.
        m = re.match(r"(.+) -> (.+)", line)
        if m:
            instructions_dict[m.group(2)] = m.group(1)
        else:
            logger.warning(f"Failed to parse line: {line}")
    return instructions_dict


def evaluate(wire: str, instructions: dict[str, str], wires: dict[str, int]) -> int:
    """
    Recursively evaluates the value of the given wire based on circuit instructions.

    If already known, returns from cache.

    :param wire: The identifier of the wire.
    :param instructions: Dictionary of instructions for each wire.
    :param wires: The cache dictionary for compound value of each wire.
    :return: The evaluated signal value for the wire.
    """
    # If the wire is a digit, return its value
    if wire.isdigit():
        return int(wire)

    # If the wire already has a value, return it
    if wire in wires:
        return wires[wire]

    # Find the instruction for the wire
    expression = instructions[wire]

    # Parse the instruction and evaluate based on the operation
    if "AND" in expression:
        a, b = expression.split(" AND ")
        value = evaluate(a, instructions, wires) & evaluate(b, instructions, wires)
    elif "OR" in expression:
        a, b = expression.split(" OR ")
        value = evaluate(a, instructions, wires) | evaluate(b, instructions, wires)
    elif "LSHIFT" in expression:
        a, n = expression.split(" LSHIFT ")
        value = evaluate(a, instructions, wires) << int(n)
    elif "RSHIFT" in expression:
        a, n = expression.split(" RSHIFT ")
        value = evaluate(a, instructions, wires) >> int(n)
    elif "NOT" in expression:
        _, a = expression.split("NOT ")
        value = (
            ~evaluate(a, instructions, wires) & 0xFFFF
        )  # 16-bit NOT using bitwise operator
    else:
        value = evaluate(expression, instructions, wires)

    # Cache value for future reference
    wires[wire] = value
    return value


@timed()
def part_2(instructions: list[str]) -> int:
    """
    Evaluates the circuit described by the provided instructions for part 2 of the puzzle.

    :param instructions: List of strings representing the instructions for the circuit.
    :return: The signal value ultimately provided to wire 'a' after overriding wire 'b'.
    """
    instructions_dict = parse_instructions(instructions)

    wires = {}

    # Get a value (part 1), should be cached
    initial_a_value = evaluate("a", instructions_dict, wires)
    logger.info(f"Initial value of wire 'a': {initial_a_value}")

    # Override with value of 'b' wire
    wires = {}  # reset cache
    wires["b"] = initial_a_value
    logger.info(f"Overriding wire 'b' with value: {wires['b']}")

    result = evaluate("a", instructions_dict, wires)

    return result


if __name__ == "__main__":
    main()
