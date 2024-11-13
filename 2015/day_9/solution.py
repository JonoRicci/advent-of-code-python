"""
Day 09

"""

import sys
import os
import itertools

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
    get_puzzle_input(2015, 9)

    # Load puzzle input via the helper module
    puzzle_input = load_input.load_puzzle_input_as_list(2015, 9)

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
def part_1(puzzle_input: list[str]) -> int:
    """
    Calculate the shortest route that visits all locations exactly once.

    :param puzzle_input: List of strings representing distances between locations
    :return: The shortest distance of visiting all locations
    """
    # Parse distances from the input
    distances = parse_distances(puzzle_input)
    logger.debug(f"Parsed distances: {distances}")
    locations = list(distances.keys())
    shortest_distance = float('inf')

    # Find the shortest route
    # Big O: O(N!) - generating all possible options
    for perm in itertools.permutations(locations):
        distance = calculate_route_distance(perm, distances)
        logger.debug(f"Checking route {perm} with distance {distance}")
        if distance < shortest_distance:
            shortest_distance = distance
            logger.debug(f"New shortest distance found: {shortest_distance}")

    return shortest_distance


def parse_distances(puzzle_input: list[str]) -> dict:
    """
    Parse the input into a dictionary of distances.

    :param puzzle_input: List of strings representing distances between locations
    :return: Dictionary with locations as keys and distances as values
    """
    distances = {}
    # Big O: O(N) - generating list length
    for line in puzzle_input:
        # Split line into components
        parts = line.split(" ")
        location_1, location_2, distance = parts[0], parts[2], int(parts[4])

        # Add distances to both directions
        if location_1 not in distances:
            distances[location_1] = {}
        if location_2 not in distances:
            distances[location_2] = {}

        distances[location_1][location_2] = distance
        distances[location_2][location_1] = distance
        logger.debug(f"Added distance: {location_1} to {location_2} = {distance}")

    return distances


def calculate_route_distance(route: tuple, distances: dict) -> int:
    """
    Calculate the total distance for a given route.

    :param route: Tuple representing a sequence of locations
    :param distances: Dictionary of distances between locations
    :return: Total distance of the route
    """
    total_distance = 0
    # Sum distances between consecutive locations in the route
    # Big O: O(N) - generating list length
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
        logger.debug(f"Adding distance from {route[i]} to {route[i + 1]}: {distances[route[i]][route[i + 1]]}, total so far: {total_distance}")

    return total_distance


@timed()
def part_2(puzzle_input: list[str]) -> int:
    """
    Calculate the longest route that visits all locations exactly once.

    :param puzzle_input: List of strings representing distances between locations
    :return: The longest distance of visiting all locations
    """
    # Parse distances from the input
    distances = parse_distances(puzzle_input)
    logger.debug(f"Parsed distances: {distances}")
    locations = list(distances.keys())
    longest_distance = 0

    # Find the longest route
    # Big O: O(N!) - generating all possible options
    for perm in itertools.permutations(locations):
        distance = calculate_route_distance(perm, distances)
        logger.debug(f"Checking route {perm} with distance {distance}")
        if distance > longest_distance:
            longest_distance = distance
            logger.debug(f"New longest distance found: {longest_distance}")

    return longest_distance


if __name__ == "__main__":
    main()
