"""
Helper logger sets up logging for the internal Helper module.
This avoids each solution having to pass the solution logger over.
"""

# TODO: I don't think I have handled logging the right way, I should improve the situation. If I have helper_logger.propagate set to True then I receive double log messages.

import logging
import sys

# Set up a default logger for the helper module
log_format = logging.Formatter("[%(asctime)s] [%(levelname)s] - %(message)s")

helper_logger = logging.getLogger("jono_aoc_helpers")
helper_logger.setLevel("DEBUG")

# Only add a handler if no handlers exist
if not helper_logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel("DEBUG")
    handler.setFormatter(log_format)
    helper_logger.addHandler(handler)

# Disable propagation to prevent double logging
helper_logger.propagate = False
