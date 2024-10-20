"""
Arguments module for Jono's Advent Of Code.
Designed to set up debug logging if instructed.
"""

import argparse


def get_arguments() -> argparse.Namespace:
    """
    Grab command line arguments and return as namespace.

    :return: Arguments object
    :rtype: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description="Set debug logging.")
    parser.add_argument("-l", "--level", type=str, help="Set logging level", default=1)
    return parser.parse_args()
