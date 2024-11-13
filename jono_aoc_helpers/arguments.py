"""
jono_aoc_helpers.arguments
--------------------------

This module gathers command line arguments to pass into daily solutions.
"""

import argparse


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

    return args
