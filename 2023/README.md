<!-- Centred Header Block -->
<div align="center">
  <h1>2023</h1>
</div>
<!-- End of Centred Header Block -->

## Table of Contents <!-- omit in toc -->

- [Usage](#usage)
  - [Running a solution](#running-a-solution)
  - [Logging](#logging)

## Usage

To get started, follow these commands to set up the Python environment. This will run jobs from the `Makefile` to automatically install python versions, set up dependencies and locally install my `jono_aoc_helpers` python package.

```shell
$ pwd
/advent-of-code-python
$ cd 2023 && pwd
/advent-of-code-python/2023
# Run helper for python version, venv, dependencies
$ make setup
✅ Development environment ready to go!
```

### Running a solution

All solutions are designed to be ran from the root year folder.

```shell
$ pwd
/advent-of-code-python/2023
$ python day_00_template/day_00.py
```

### Logging

You can select the log level by passing in an argument with `-l` or `--log-level`

```shell
$ pwd
/advent-of-code-python/2023
$ python day_00_template/day_00.py -l DEBUG
$ python day_00_template/day_00.py --log-level DEBUG
```

The accepted inputs are:

```none
DEBUG
INFO
WARN
ERROR
```
