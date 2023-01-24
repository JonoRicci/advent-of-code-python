"""
Day 03

"""
from logger import logger


def main() -> None:
    """
    Import the puzzle input, process and display the results.

    """
    diagnostic_report = import_list()

    power_consumption = calculate_power_consumption(diagnostic_report)
    logger.info(f"Part 01: The power consumption is: {power_consumption}.")
    life_support_rating = calculate_life_support_rating(diagnostic_report)
    logger.info(f"Part 02: The life support rating is: {life_support_rating}.")


def import_list() -> list:
    """
    Import the puzzle input and return a list.

    :return: Puzzle input text file as list
    :rtype: list
    """
    file = open("puzzle-input", "r")
    string_list = file.read().splitlines()
    file.close()
    return string_list


def calculate_power_consumption(report: list) -> int:
    """
    Receive a binary list. Create two dictionaries to track count of 1s and 0s
    in each column of the line.

    There are 12 columns (12 chars).

    Calculate the gamma and epsilon rates, convert both values to decimal and
    multiply.

    :param report: List of binary strings
    :return: Power consumption
    :rtype: int
    """

    gamma = ""
    epsilon = ""
    count_0 = {}
    count_1 = {}

    for line in report:
        # Column tracks column position, value tracks 1 or 0.
        for column, value in enumerate(line):
            # Populate the counts.
            if column not in count_0:
                count_0[column] = 0
            if column not in count_1:
                count_1[column] = 0
            if value == "1":
                count_1[column] += 1
            else:
                count_0[column] += 1

    for value in count_0:
        if count_0[value] > count_1[value]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    logger.debug(
        (f"Gamma: {gamma, int(gamma, 2)}, " f"Epsilon: {epsilon, int(epsilon, 2)}")
    )
    # Convert binary (base 2) to integers.
    power_consumption = int(gamma, 2) * int(epsilon, 2)
    return power_consumption


def calculate_life_support_rating(report: list) -> int:
    """
    Receive a binary list. Traverse the list twice, the first time applying the
    oxygen conditions and the second time applying the co2 conditions and saving
    these to separate lists.

    Use nested list comprehension to check:
        for character in binary string:
            if character's value is 0:
                return character (append to list)

    Then do the final conditions to get 0 or 1. Convert to ints and multiply to
    get life support rating.

    :param report: List of binary strings
    :return: Life support rating
    :rtype: int
    """

    oxygen_list = report
    co2_list = report

    for value in range(len(report[0])):
        if len(oxygen_list) > 1:
            oxygen_list_0 = len([char for char in oxygen_list if char[value] == "0"])
            oxygen_list_1 = len([char for char in oxygen_list if char[value] == "1"])
            if oxygen_list_1 >= oxygen_list_0:
                oxygen_list = [char for char in oxygen_list if char[value] == "1"]
            else:
                oxygen_list = [char for char in oxygen_list if char[value] == "0"]

        if len(co2_list) > 1:
            co2_list_0 = len([char for char in co2_list if char[value] == "0"])
            co2_list_1 = len([char for char in co2_list if char[value] == "1"])
            if co2_list_1 >= co2_list_0:
                co2_list = [char for char in co2_list if char[value] == "0"]
            else:
                co2_list = [char for char in co2_list if char[value] == "1"]

    oxygen_generator_rating = oxygen_list[0]
    co2_scrubber_rating = co2_list[0]

    logger.debug(
        f"Oxygen Generator Rating: {oxygen_generator_rating, int(oxygen_generator_rating, 2)}, "
        f"CO2 Scrubber Rating: {co2_scrubber_rating, int(co2_scrubber_rating, 2)}"
    )

    life_support_rating = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
    return life_support_rating


if __name__ == "__main__":
    main()
