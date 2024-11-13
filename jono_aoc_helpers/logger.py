"""
jono_aoc_helpers.logging
------------------------

This module sets up logging for the daily solution.
"""

import logging
import sys
import os
from typing import Optional


def initiate_logging(
    level: str = "INFO", log_file: Optional[str] = None
) -> logging.Logger:
    """
    Initiate a logger instance which can accept a logging level parameter.

    :param level: Logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
    :param log_file: Optional file path to write the logs to
    :return: Logging object
    """

    # Use environment variable or default to INFO
    level = level or os.getenv("AOC_LOG_LEVEL", "INFO")

    # Validate the logging level
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {level}")

    log_format = logging.Formatter("[%(asctime)s] [%(levelname)s] - %(message)s")

    # Stream handler for console output
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(numeric_level)
    handler.setFormatter(log_format)

    # Get a logger with the current module's name
    logger = logging.getLogger(__name__)
    logger.setLevel(numeric_level)

    # Avoid adding duplicate handlers
    if not logger.hasHandlers():
        logger.addHandler(handler)

    # File handler for writing logs to a file (if log_file is provided)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(numeric_level)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)

    # Prevent log messages from being passed to the root logger multiple times
    logger.propagate = False

    return logger


LoggerType = logging.Logger
