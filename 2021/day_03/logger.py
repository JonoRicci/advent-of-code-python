"""
Logging module for Jono's Advent Of Code.
"""

import logging
import sys

level = logging.INFO
logging.getLogger().setLevel(level)
log_format = logging.Formatter("[%(asctime)s] [%(levelname)s] - %(message)s")

logger = logging.getLogger()

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(level)
handler.setFormatter(log_format)

logger.addHandler(handler)
