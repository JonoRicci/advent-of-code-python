"""
Day 01

"""


def main() -> None:
    """
    Import the puzzle input, process and display the results.

    """
    depth_list = import_list()

    increases = count_increases(depth_list)
    print(f"Part 01: There were {increases} increases in depth.")

    sliding_increases = count_sliding_increases(depth_list)
    print(f"Part 02: There were {sliding_increases} sliding increases in depth.")


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


def count_increases(depths: list):
    """
    Count the number of times a value is greater than the previous value.

    :param depths: list of depths
    :return: number of times depth increased
    :rtype: int
    """
    increases = 0
    previous = None

    for depth in depths:
        depth = int(depth)
        if previous and depth > previous:
            increases += 1
        previous = depth

    return increases


def count_sliding_increases(depths: list):
    """

    :param depths: list of depths
    :return: number of times depth increased
    :rtype: int
    """
    increases = 0
    int_depths = [int(depth) for depth in depths]

    for position in range(len(int_depths)):
        if (
            position >= 3
            and int_depths[position]
            + int_depths[position - 1]
            + int_depths[position - 2]
            > int_depths[position - 1]
            + int_depths[position - 2]
            + int_depths[position - 3]
        ):
            increases += 1

    return increases


if __name__ == "__main__":
    main()
