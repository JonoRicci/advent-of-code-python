"""
jono_aoc_helpers.arguments
--------------------------

This module gathers command line arguments to pass into daily solutions.
"""

import argparse
import logging


def get_arguments() -> argparse.Namespace:
    """
    Grab command line arguments and return as namespace.

    :return: Arguments object
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description="Set debug logging.")
    parser.add_argument(
        "-l",
        "--level",
        type=str,
        help="Set logging level (e.g., DEBUG, INFO, WARNING)",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    )

    args = parser.parse_args()

    # Set up logging level based on provided argument
    numeric_level = getattr(logging, args.level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(
            f"Invalid log level: {args.level}. "
            f"Choose from DEBUG, INFO, WARNING, ERROR, CRITICAL."
        )
    logging.basicConfig(level=numeric_level)

    return args
