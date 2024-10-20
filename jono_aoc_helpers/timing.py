"""
Timing Decorator for measuring execution time of functions.
"""

import time
from functools import wraps
from typing import Callable
from .helper_logger import helper_logger



def timed() -> Callable:
    """
    A decorator to measure the execution time of a function.

    :return: The wrapped function with timing logic.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time

            helper_logger.info(
                f"Time taken by {func.__name__}: {elapsed_time:.4f} seconds"
            )
            return result

        return wrapper

    return decorator