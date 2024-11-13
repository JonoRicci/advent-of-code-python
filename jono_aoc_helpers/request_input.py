"""
jono_aoc_helpers.request_input
------------------------------

This module fetches the puzzle input from the Advent of Code website and writes it to a file.
"""

# !/usr/bin/python3
import logging
import os
import requests
from typing import Optional
import time

# Find SESSION via Firefox:
# 1. Navigate to https://adventofcode.com/2022/day/1/input
# 2. From Developer tools navigate to Network
# 3. Grab the "session" cookie.
# 4. Export as environment variable
SESSION: Optional[str] = os.getenv("AOC_SESSION")

logger = logging.getLogger(__name__)


def get_puzzle_input(
    year: int, day: int, retry_attempts: int = 3, retry_delay: int = 5
) -> None:
    """
    Get puzzle input for the specified year and day, and write it to a file. If the file already exists, do not request the input again to avoid unnecessary requests.

    :param year: Year of the puzzle
    :param day: Day of the puzzle
    :param retry_attempts: Number of retry attempts if the request fails
    :param retry_delay: Delay in seconds between retry attempts
    """

    # Validate year and day
    if year < 2015 or day < 1 or day > 25:
        logger.error(
            "Invalid year or day. Year must be >= 2015 and day must be between 1 and 25."
        )
        return

    # Check if SESSION token is present
    if not SESSION:
        logger.error(
            "SESSION environment variable is empty. Please set it by exporting your Advent of Code session cookie as an environment variable: export AOC_SESSION=<your_session_cookie>. You can get the cookie by inspecting cookies from the browser while on the Advent of Code website puzzle input page."
        )
        raise SystemExit("SESSION cookie missing. Ending program.")

    # Define the file path relative to the root directory of the year folder
    file_name = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        str(year),
        f"day_{day}",
        "puzzle-input",
    )

    # Check if the input file already exists
    if os.path.exists(file_name):
        logger.info(f"Input for {year}, day {day} already exists: {file_name}")
        return

    # Fetch the puzzle input using requests with retry logic
    attempt = 0
    while attempt < retry_attempts:
        try:
            response = requests.get(
                f"https://adventofcode.com/{year}/day/{day}/input",
                cookies={"session": SESSION},
            )
            response.raise_for_status()
            puzzle_input = response.text
            break
        except requests.RequestException as e:
            attempt += 1
            if attempt < retry_attempts:
                logger.warning(
                    f"Attempt {attempt} failed: {e}. Retrying in {retry_delay} seconds..."
                )
                time.sleep(retry_delay)
            else:
                logger.error(
                    f"Failed to fetch input after {retry_attempts} attempts: {e}"
                )
                return

    # Ensure the directory for the day exists
    try:
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
    except OSError as e:
        logger.error(f"Failed to create directory for file {file_name}: {e}")
        return

    # Write puzzle input to a file
    try:
        with open(file_name, "w") as file:
            file.write(puzzle_input)
            logger.info(
                f"Puzzle input for year {year}, day {day} has been successfully written to {file_name}"
            )
    except OSError as e:
        logger.error(f"Failed to write input to file {file_name}: {e}")
