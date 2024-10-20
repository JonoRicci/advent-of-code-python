<!-- Centred Header Block -->
<div align="center">
  <h1>Jono's Advent Of Code Python Solutions</h1>
  <p align="center">
    My attempts at the problems from <a href="https://adventofcode.com/">Advent of Code</a>. Solutions are organised by year and problem.
  </p>
</div>
<!-- End of Centred Header Block -->

## Table of Contents <!-- omit in toc -->

- [Solutions](#solutions)
- [Setup](#setup)
  - [Requirements](#requirements)
  - [Installation](#installation)
- [Usage](#usage)
  - [Helper Module](#helper-module)
- [Puzzle Inputs](#puzzle-inputs)

## Solutions

Links to each of my completed solutions.

| Day | 2024 | 2023 | 2022 | 2021 | 2020 | 2019 | 2018 | 2017 | 2016 | 2015 |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 |  |  | [✅][22d01] | [✅][21d01] | [✅][20d01] |  |  |  |  |  |
| 02 |  |  | [✅][22d02] | [✅][21d02] | [✅][20d02] |  |  |  |  |  |
| 03 |  |  |  | [✅][21d03] | [✅][20d03] |  |  |  |  |  |
| 04 |  |  |  | [✅][21d04] | [✅][20d04] |  |  |  |  |  |
| 05 |  |  |  | [✅][21d05] | [✅][20d05] |  |  |  |  |  |
| 06 |  |  |  | [✅][21d06] | [✅][20d06] |  |  |  |  |  |
| 07 |  |  |  | [✅][21d07] | [✅][20d07] |  |  |  |  |  |
| 08 |  |  |  |  | [✅][20d08] |  |  |  |  |  |
| 09 |  |  |  |  | [✅][20d09] |  |  |  |  |  |
| 10 |  |  |  |  | [✅][20d10] |  |  |  |  |  |
| 11 |  |  |  |  | [✅][20d11] |  |  |  |  |  |
| 12 |  |  |  |  |  |  |  |  |  |  |
| 13 |  |  |  |  |  |  |  |  |  |  |
| 14 |  |  |  |  |  |  |  |  |  |  |
| 15 |  |  |  |  |  |  |  |  |  |  |
| 16 |  |  |  |  |  |  |  |  |  |  |
| 17 |  |  |  |  |  |  |  |  |  |  |
| 18 |  |  |  |  |  |  |  |  |  |  |
| 19 |  |  |  |  |  |  |  |  |  |  |
| 20 |  |  |  |  |  |  |  |  |  |  |
| 21 |  |  |  |  |  |  |  |  |  |  |
| 22 |  |  |  |  |  |  |  |  |  |  |
| 23 |  |  |  |  |  |  |  |  |  |  |
| 24 |  |  |  |  |  |  |  |  |  |  |

## Setup

If you are interested in running these solutions locally on your machine following the steps below.

### Requirements

Ensure you have access or installed:

- [pyenv][pyenv] (to manage multiple versions of python)
  - There is a `.python-version` file in each year's folder, which will instruct pyenv on what version to use.
- A shell environment (e.g., Bash, Zsh)
- [Make][make] (to automate tasks via the Makefile)
- [Git][git] (to clone the repo)
-

### Installation

All you need to do is clone the repo.

```shell
git clone git@github.com:JonoRicci/advent-of-code-python.git
```

## Usage

Each year is treated as a seperate python environment, with it's own configuration, virtual environment, dependencies and python version. This is because I only visit this repo yearly in December, and I don't want to do maintenance on all my previous solutions if I want to upgrade Python for the current year or change something else.

The year folder is the root directory, and all commands to execute the solutions are intended to be run from the year root directory.

Check the README for each year for specific usage.

- [📖 2023 README][23rdme]
- [📖 2022 README][22rdme]
- [📖 2021 README][21rdme]
- [📖 2020 README][20rdme]
- [📖 2019 README][19rdme]
- [📖 2018 README][18rdme]
- [📖 2017 README][17rdme]
- [📖 2016 README][16rdme]
- [📖 2015 README][15rdme]

### Helper Module

I have library of common functions that I've packaged as a local helper module.

Setup to use this library is included in the yearly README files.

## Puzzle Inputs

My puzzle inputs are not included in this repository, they are ignored via my `.gitignore` file. My puzzle answers are included, as they are used in my tests to validate the solution works.

Please see the [Advent of Code 2024 FAQ][faq].

> Can I copy/redistribute part of Advent of Code? Please don't. Advent of Code is free to use, not free to copy. If you're posting a code repository somewhere, please don't include parts of Advent of Code like the puzzle text or your inputs. If you're making a website, please don't make it look like Advent of Code or name it something similar.

<!-- Links -->

[22d01]: 2022/day_01/
[22d02]: 2022/day_02/

[21d01]: 2021/day_01/
[21d02]: 2021/day_02/
[21d03]: 2021/day_03/
[21d04]: 2021/day_04/
[21d05]: 2021/day_05/
[21d06]: 2021/day_06/
[21d07]: 2021/day_07/

[20d01]: 2020/day-01/
[20d02]: 2020/day-02/
[20d03]: 2020/day-03/
[20d04]: 2020/day-04/
[20d05]: 2020/day-05/
[20d06]: 2020/day-06/
[20d07]: 2020/day-07/
[20d08]: 2020/day-08/
[20d09]: 2020/day-09/
[20d10]: 2020/day-10/
[20d11]: 2020/day-11/

[faq]: https://adventofcode.com/2024/about
[pyenv]: https://github.com/pyenv/pyenv
[make]: https://www.gnu.org/software/make/
[git]: https://git-scm.com/

[23rdme]: 2023/README.md
[22rdme]: 2022/README.md
[21rdme]: 2021/README.md
[20rdme]: 2020/README.md
[19rdme]: 2019/README.md
[18rdme]: 2018/README.md
[17rdme]: 2017/README.md
[16rdme]: 2016/README.md
[15rdme]: 2015/README.md
