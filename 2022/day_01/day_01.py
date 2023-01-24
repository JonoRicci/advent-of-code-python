"""
Day 01

"""
from logger import logger


def main() -> None:
    """
    Import the puzzle input, process and display the results.

    """
    puzzle_input = import_list("puzzle-input")
    logger.debug(puzzle_input)
    total_calories_list = count_elf_calories(puzzle_input)

    most_calories = get_max_calories(total_calories_list)
    logger.info(f"Part One: The elf with the most calories has: {most_calories}")

    combined_backup_calories = get_combined_backup_calories(total_calories_list)
    logger.info(
        f"Part Two: The top three Elves combined calories amounts to: {combined_backup_calories}"
    )


def import_list(filename: str) -> list:
    """
    Import the puzzle input and return a list.

    :param filename: file with puzzle input
    :return: Puzzle input text file as list
    :rtype: list
    """
    with open(filename, "r") as file:
        string_list = file.read().splitlines()
    return string_list


def count_elf_calories(puzzle_input: list) -> list:
    """
    Return a list of each elf's combined calories.

    :param puzzle_input: puzzle input from file
    :return: Each elf's combined calories
    :rtype: list
    """
    total_calories_list = []
    for elf in ("\n".join(puzzle_input)).split("\n\n"):
        logger.debug(elf.split("\n"))
        total_calories = 0
        for food_calories in elf.split("\n"):
            total_calories += int(food_calories)
        total_calories_list.append(total_calories)
    return total_calories_list


def get_max_calories(total_calories_list: list) -> int:
    """
    Return the element in a list with the max value.

    :param total_calories_list: list of integers of total calories per elf
    :return: Max value from list
    :rtype: int
    """
    return max(total_calories_list)


def get_combined_backup_calories(total_calories_list: list) -> int:
    """
    Return the combined value of second, third and forth greatest calories count.

    :param total_calories_list: list of integers of total calories per elf
    :return: Combined value of calories
    :rtype: int
    """
    sorted_calories = sorted(total_calories_list)
    return sorted_calories[-1] + sorted_calories[-2] + sorted_calories[-3]


if __name__ == "__main__":
    main()
