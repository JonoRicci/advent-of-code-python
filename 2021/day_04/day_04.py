"""
Day 04

"""
from logger import logger


def main() -> None:
    """
    Import the puzzle input, process and display the results.

    """
    puzzle_input = import_list()
    logger.debug(puzzle_input)
    final_score = play_bingo(puzzle_input)
    for result in final_score:
        logger.info(f"The final score is: {result}.")


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


def play_bingo(bingo_cards: list) -> list:
    """
    Extract winning numbers, bingo boards from input.
    Make a separate 2D list tracking wins.
    For each winning number, check every board row and column for a match.
    Add matches to the 2D list tracking wins.
    Once done, check 2D list for winning columns / rows.
    Add winning boards to new list along with winning number.
    Multiply to get score.

    :param bingo_cards: puzzle input where each line is a string
    :return: First and last winning board score
    :rtype: list
    """

    winning_numbers = [int(x) for x in bingo_cards[0].split(",")]
    logger.debug(f" Winning numbers: {winning_numbers}")

    single_board = []
    all_boards = []
    final_score_list = []

    # Get Bingo Boards
    for line in range(len(bingo_cards)):
        if "," not in bingo_cards[line]:
            row = [int(x) for x in bingo_cards[line].split()]
            if row:
                logger.debug(row)
                single_board.append(row)
            elif single_board:
                all_boards.append(single_board)
                single_board = []

    # Set up separate 2D list tracking matches to winning numbers.
    unmarked_tracker = []
    for board in all_boards:
        assert len(board) == 5 and len(board[0]) == 5
        unmarked_tracker.append([[False for _ in range(5)] for _ in range(5)])

    # Set up list to track winning boards.
    winning_board = [False for _ in range(len(all_boards))]

    for number in winning_numbers:
        for index, board in enumerate(all_boards):
            logger.debug(f"Checking board: {index} for {number}")

            # Check for winning numbers.
            for row in range(5):
                for column in range(5):
                    if board[row][column] == number:
                        logger.debug(
                            f"{unmarked_tracker[index][row][column]} " f"is True."
                        )
                        unmarked_tracker[index][row][column] = True

            # Check for 5 in a row.
            won = False
            for row in range(5):
                ok = True
                for column in range(5):
                    if not unmarked_tracker[index][row][column]:
                        ok = False
                if ok:
                    won = True

            # Check for 5 in a column.
            for column in range(5):
                ok = True
                for row in range(5):
                    if not unmarked_tracker[index][row][column]:
                        ok = False
                if ok:
                    won = True

            # Check for each winning board.
            if won and not winning_board[index]:
                winning_board[index] = True
                winning_boards_count = len(
                    [j for j in range(len(all_boards)) if winning_board[j]]
                )

                # If first or last board.
                if winning_boards_count == 1 or winning_boards_count == len(all_boards):
                    # Calculate all unmarked.
                    unmarked = 0
                    for row in range(5):
                        for column in range(5):
                            if not unmarked_tracker[index][row][column]:
                                unmarked += board[row][column]

                    final_score_list.append(unmarked * number)
                    logger.debug(
                        f"The final score is: {final_score_list[-1]}, "
                        f"which is {unmarked} * {number}."
                    )

    return final_score_list


if __name__ == "__main__":
    main()
