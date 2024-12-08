<!-- Centred Header Block -->
<div align="center">
  <a href="https://github.com/jonoricci/advent-of-code-python">
    <img src="./docs/readme_assets/Title.png" alt="Logo" height="300">
  </a>
  <p>
    <img src="https://img.shields.io/badge/2015-18/50-green" alt="2015: 18/50">
    <img src="https://img.shields.io/badge/2016-0/50-lightgrey" alt="2016: 0/50">
    <img src="https://img.shields.io/badge/2017-0/50-lightgrey" alt="2017: 0/50">
    <img src="https://img.shields.io/badge/2018-0/50-lightgrey" alt="2018: 0/50">
    <img src="https://img.shields.io/badge/2019-0/50-lightgrey" alt="2019: 0/50">
    <img src="https://img.shields.io/badge/2020-22/50-green" alt="2020: 22/50">
    <img src="https://img.shields.io/badge/2021-14/50-green" alt="2021: 14/50">
    <img src="https://img.shields.io/badge/2022-4/50-yellow" alt="2022: 4/50">
    <img src="https://img.shields.io/badge/2023-0/50-lightgrey" alt="2023: 0/50">
    <img src="https://img.shields.io/badge/2024-2/50-yellow" alt="2024: 2/50">
  </p>
  <p align="center">
    My attempts at the problems from <a href="https://adventofcode.com/">Advent of Code</a> using <em>Python</em>. Solutions are organised by year and day.
  </p>
  <p>
    These solutions prioritise readability, maintainability, and real-world practices over speed of writing or competitive programming techniques. The goal is to craft production ready code, similar to what I'd write in my professional role.
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
- [Execution Time](#execution-time)
- [Puzzle Inputs](#puzzle-inputs)
- [Links](#links)

## Solutions

Links to each of my completed solutions.

| Day | 2024 | 2023 | 2022 | 2021 | 2020 | 2019 | 2018 | 2017 | 2016 | 2015 |
|---|---|---|---|---|---|---|---|---|---|---|
| 01 | [⭐⭐][24d01] |  | [⭐⭐][22d01] | [⭐⭐][21d01] | [⭐⭐][20d01] |  |  |  |  | [⭐⭐][15d01] |
| 02 | [⭐⭐][24d02] |  | [⭐⭐][22d02] | [⭐⭐][21d02] | [⭐⭐][20d02] |  |  |  |  | [⭐⭐][15d02] |
| 03 | [⭐⭐][24d03] |  |  | [⭐⭐][21d03] | [⭐⭐][20d03] |  |  |  |  | [⭐⭐][15d03]  |
| 04 |  |  |  | [⭐⭐][21d04] | [⭐⭐][20d04] |  |  |  |  | [⭐⭐][15d04] |
| 05 |  |  |  | [⭐⭐][21d05] | [⭐⭐][20d05] |  |  |  |  | [⭐⭐][15d05] |
| 06 |  |  |  | [⭐⭐][21d06] | [⭐⭐][20d06] |  |  |  |  | [⭐⭐][15d06] |
| 07 |  |  |  | [⭐⭐][21d07] | [⭐⭐][20d07] |  |  |  |  | [⭐⭐][15d07] |
| 08 |  |  |  |  | [⭐⭐][20d08] |  |  |  |  | [⭐⭐][15d08] |
| 09 |  |  |  |  | [⭐⭐][20d09] |  |  |  |  | [⭐⭐][15d09] |
| 10 |  |  |  |  | [⭐⭐][20d10] |  |  |  |  |  |
| 11 |  |  |  |  | [⭐⭐][20d11] |  |  |  |  |  |
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

### Installation

All you need to do is clone the repo.

```shell
git clone git@github.com:JonoRicci/advent-of-code-python.git
```

## Usage

Each year has its own isolated Python environment with a specific configuration, virtual environment, dependencies, and Python version. I only work on this repository once a year in December, so this setup allows me to upgrade Python or adjust configurations for the current year without needing to update or maintain solutions from previous years.

The year folder is the root directory, and all commands to execute the solutions are intended to be run from the year root directory.

Check the README for each year for specific usage.

- [📖 2024 README][24rdme]
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

I have library of common Advent of Code functions that I've packaged as a local helper module `jono_aoc_helpers`. It includes such helpers as:

- ⬇️ Automatic puzzle input retrieval and caching
- 💾 Writing puzzle input to a file
- 🔍 Loading puzzle input in multiple data types
- 📖 Initiating logging
- 🛠️ Gathering command line arguments
- ⏰ Timing function execution time

These are included in the skeleton template files when setting up new day solutions. You can read more below:

- [📖 Jono's AoC Helper Module README][jono_aoc_helper]

## Execution Time

I record the execution time of each part of a day's solution. You can view these below:

- [⏰ 2015 Solution Execution Times][15times]

## Puzzle Inputs

My puzzle inputs are not included in this repository, they are ignored via my `.gitignore` file. My puzzle answers are included, as they are used in my tests to validate the solution works.

Please see the [Advent of Code 2024 FAQ][faq].

> Can I copy/redistribute part of Advent of Code? Please don't. Advent of Code is free to use, not free to copy. If you're posting a code repository somewhere, please don't include parts of Advent of Code like the puzzle text or your inputs. If you're making a website, please don't make it look like Advent of Code or name it something similar.

## Links

- https://old.reddit.com/r/adventofcode/comments/1gsl4fm/share_your_favorite_tricks_and_snippets/

<!-- Links -->

[24d01]: 2024/day_01/
[24d02]: 2024/day_02/
[24d03]: 2024/day_03/

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

[15d01]: 2015/day_1/
[15d02]: 2015/day_2/
[15d03]: 2015/day_3/
[15d04]: 2015/day_4/
[15d05]: 2015/day_5/
[15d06]: 2015/day_6/
[15d07]: 2015/day_7/
[15d08]: 2015/day_8/
[15d09]: 2015/day_9/

[faq]: https://adventofcode.com/2024/about
[pyenv]: https://github.com/pyenv/pyenv
[make]: https://www.gnu.org/software/make/
[git]: https://git-scm.com/

[24rdme]: 2024/README.md
[23rdme]: 2023/README.md
[22rdme]: 2022/README.md
[21rdme]: 2021/README.md
[20rdme]: 2020/README.md
[19rdme]: 2019/README.md
[18rdme]: 2018/README.md
[17rdme]: 2017/README.md
[16rdme]: 2016/README.md
[15rdme]: 2015/README.md

[15times]: docs/Execution%20Times/2015.md

[jono_aoc_helper]: jono_aoc_helpers/README.md
