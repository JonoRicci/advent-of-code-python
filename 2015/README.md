<!-- Centred Header Block -->
<div align="center">
  <a href="https://github.com/jonoricci/advent-of-code-python">
    <img src="../docs/readme_assets/2015.png" alt="Logo" height="200">
  </a>
</div>
<!-- End of Centred Header Block -->

## Table of Contents <!-- omit in toc -->

- [Usage](#usage)
  - [Running a solution](#running-a-solution)
  - [Logging](#logging)
  - [Clean up](#clean-up)
  - [Make new solution skeleton](#make-new-solution-skeleton)

## Usage

To get started, follow these commands to set up the Python environment. This will run jobs from the `Makefile` to automatically install python versions, set up dependencies and locally install my `jono_aoc_helpers` python package.

```shell
$ pwd
/advent-of-code-python
$ cd 2015 && pwd
/advent-of-code-python/2015
# Run helper for python version, venv, dependencies
$ make setup
✅ Development environment ready to go!
```

### Running a solution

All solutions are designed to be ran from the root year folder.

```shell
$ pwd
/advent-of-code-python/2015
$ python day_00_template/day_00.py
```

### Logging

You can select the log level by passing in an argument with `-l` or `--log-level` or by setting an environment variable `AOC_LOG_LEVEL`.

If not specified then the default behaviour is `INFO`.

```shell
# Command line argument
$ pwd
/advent-of-code-python/2015
$ python day_00_template/day_00.py -l DEBUG
$ python day_00_template/day_00.py --log-level DEBUG

# Environment variable
export AOC_LOG_LEVEL=DEBUG
```

The accepted inputs are:

```none
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

### Clean up

If for any reason you need to remove the virtual environment and start again, you can run the following:

```shell
$ pwd
/advent-of-code-python/2015
$ make clean
```

### Make new solution skeleton

When starting a new problem, you can run the following command to set up the subdirectory and create a skeleton solution file:

```shell
$ pwd
/advent-of-code-python/2015
$ make newday DAY=3
```
