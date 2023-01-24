"""
Day 02

"""
from logger import logger


def main() -> None:
    """
    Import the puzzle input, process and display the results.

    """
    puzzle_input = import_list("puzzle-input")
    logger.debug(puzzle_input)

    always_win_score = get_always_win_score(puzzle_input)
    logger.info(f"Part One: The score is {always_win_score}")

    tactical_score = get_tactical_score(puzzle_input)
    logger.info(f"Part Two: The score is {tactical_score}")


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


def get_always_win_score(puzzle_input: list) -> int:
    """
    Calculate the score from the input where we always win.

    :param puzzle_input: list with puzzle input
    :return: total score from strategy guide
    :rtype: int
    """
    score = 0
    for game_round in puzzle_input:
        opponent, player = game_round.split()
        logger.debug(f"Opponent: {opponent}, Player: {player}")
        score += {"X": 1, "Y": 2, "Z": 3}[player]
        score += {
            ("A", "X"): 3,
            ("A", "Y"): 6,
            ("A", "Z"): 0,
            ("B", "X"): 0,
            ("B", "Y"): 3,
            ("B", "Z"): 6,
            ("C", "X"): 6,
            ("C", "Y"): 0,
            ("C", "Z"): 3,
        }[(opponent, player)]
    return score


def get_tactical_score(puzzle_input: list) -> int:
    """
    Calculate the score from the input where we sometimes draw or lose.

    :param puzzle_input: list with puzzle input
    :return: total score from strategy guide
    :rtype: int
    """
    score = 0
    for game_round in puzzle_input:
        opponent, player = game_round.split()
        logger.debug(f"Opponent: {opponent}, Player: {player}")
        score += {"X": 0, "Y": 3, "Z": 6}[player]
        score += {
            ("A", "X"): 3,
            ("A", "Y"): 1,
            ("A", "Z"): 2,
            ("B", "X"): 1,
            ("B", "Y"): 2,
            ("B", "Z"): 3,
            ("C", "X"): 2,
            ("C", "Y"): 3,
            ("C", "Z"): 1,
        }[(opponent, player)]
    return score


if __name__ == "__main__":
    main()
