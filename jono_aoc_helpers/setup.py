"""
jono_aoc_helpers.setup
----------------------
"""

from setuptools import setup, find_packages

setup(
    name="jono_aoc_helpers",
    version="0.1.0",
    description="Helper utilities for Advent of Code challenges.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Jonathan Ricci",
    author_email="jonathansricci@gmail.com",
    url="https://github.com/jonoricci/advent-of-code-python",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers"
    ],
    python_requires=">=3.13",
)
