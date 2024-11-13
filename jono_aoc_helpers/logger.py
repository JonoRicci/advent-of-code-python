"""
jono_aoc_helpers.logging
------------------------

This module sets up logging for the daily solution.
"""

import logging
import sys
import os
from typing import Optional


def initiate_logging(level: Optional[str] = None) -> logging.Logger:
    """
    Initiate a logger instance which can accept a logging level parameter.

    :param level: Logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
    :return: Logging object
    """
    # Use environment variable or default to INFO
    level = level or os.getenv("AOC_LOG_LEVEL", "INFO")

    # Validate the logging level
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {level}")

    # Create or get a named logger to avoid conflicts with root logger
    logger = logging.getLogger()
    logger.setLevel(numeric_level)

    # Ensure no duplicate handlers are added
    if not logger.hasHandlers():
        # Create a handler and set the formatter
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(numeric_level)
        log_format = logging.Formatter("[%(asctime)s] [%(name)s] [%(levelname)s] - %(message)s")
        handler.setFormatter(log_format)

        # Add the handler to the logger
        logger.addHandler(handler)

    return logger


# Alias for logging.Logger to use in type annotations
LoggerType = logging.Logger
