"""
Day 00

"""

# Add jono_aoc_helpers (local pip module)
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from jono_aoc_helpers import logger
from jono_aoc_helpers import arguments


def main() -> None:
    """
    Call common modules to carry out routine tasks.
    Then call solution functions.
    """
    # Set up common modules
    args = arguments.get_arguments()
    logs = logger.initiate_logging(args.level)
    logs.debug("Hello")


if __name__ == "__main__":
    main()
