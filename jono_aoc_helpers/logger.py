"""
Logging module for Jono's Advent of Code.
Designed to set up console logging for solutions.
"""

import logging
import sys


def initiate_logging(level: str = "INFO") -> logging.Logger:
    """
    Initiate a logger instance which can accept a logging level parameter.

    :param level: logging level
    :return: Logging object
    :rtype: logging.Logger
    """
    log_format = logging.Formatter("[%(asctime)s] [%(levelname)s] - %(message)s")

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    handler.setFormatter(log_format)

    logger = logging.getLogger()
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
