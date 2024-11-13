# Jono's AoC Helper Module <!-- omit in toc -->

This helper module is designed to assist with Advent of Code (AoC) challenges. Currently, it is a local module that can be imported via pip, though it is not yet versioned. This could create issues if updates are made while older challenges still depend on the existing code.

## Table of Contents <!-- omit in toc -->

- [Installation](#installation)
- [Usage](#usage)
- [To Do](#to-do)

## Installation

Currently, this module can be installed locally. Once versioned and published, installation will be straightforward via `pip`:

To install from a local copy:

```sh
pip install -e /path/to/jono_aoc_helpers
```

## Usage

To use the module, you can import the desired functionality into your puzzle scripts:

```python
# Add jono_aoc_helpers (local pip module)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from jono_aoc_helpers.load_input import load_puzzle_input_as_list
from jono_aoc_helpers.timing import timed
```

## To Do

1. **Version the module**: This will help manage dependencies and ensure that specific years call a specific version of the helpers.
   1. Decide on a publishing platform (e.g., PyPI) to make the module more widely accessible.
   2. Determine whether the module should be public or private.
2. **Add additional boilerplate**: Keep expanding on any reusable utility that could help solve Advent of Code challenges faster and more consistently.
3. Automate the readme or add some kind of automated docs.
