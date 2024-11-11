"""
Jono's Advent of Code Helpers
"""

# Set default logging handler for helper module
import logging
from logging import NullHandler

logging.getLogger(__name__).addHandler(NullHandler())
