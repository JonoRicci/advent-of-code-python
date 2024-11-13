"""
Jono's Advent of Code Helpers
-----------------------------
"""

# Set up a logger for the module with a NullHandler to avoid "No handler found"
# warnings.
import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())
