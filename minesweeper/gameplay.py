import os
import time
from typing import Tuple

import board

MIN_ROWS = 1
MAX_ROWS = 10
MIN_COLUMNS = 1
MAX_COLUMNS = 10


def get_board_parameter(message: str, minimum: int, maximum: int) -> int:
    while True:
        try:
            number = int(input(message))
            if not minimum <= number <= maximum:
                raise ValueError(f"Number not within limits: '{number}'")
        except ValueError as error:
            print(f"Error: {error}")
        else:
            break
    return number


def get_field_coordinates(minefield: board.Board) -> Tuple[int, int]:
    row = get_board_parameter(
        f"Select row ({MIN_ROWS - 1}-{minefield.rows - 1}): ",
        MIN_ROWS - 1,
        minefield.rows - 1,
    )
    column = get_board_parameter(
        f"Select column ({MIN_COLUMNS - 1}-{minefield.columns - 1}): ",
        MIN_COLUMNS - 1,
        minefield.columns - 1,
    )
    return row, column


def get_player_action(message: str, allowed_actions: list[str]) -> str:
    while True:
        try:
            char = input(message).lower()
            if not char in allowed_actions:
                raise ValueError(f"Incorrect input: {char}")
        except ValueError as error:
            print(f"Error: {error}")
        else:
            break
    return char


def create_board() -> board.Board:
    rows = get_board_parameter(
        f"Input the number of rows ({MIN_ROWS}, {MAX_ROWS}): ", MIN_ROWS, MAX_ROWS
    )
    columns = get_board_parameter(
        f"Input the number of columns ({MIN_COLUMNS}, {MAX_COLUMNS}): ",
        MIN_COLUMNS,
        MAX_COLUMNS,
    )
    mines = get_board_parameter(
        f"Input the number of mines ({1}-{rows * columns}): ", 1, rows * columns
    )
    return board.Board(rows, columns, mines)


def toggle_field_marked(field: board.Field) -> None:
    if not field.hidden:
        raise ValueError("Error: Only hidden fields may be (un)marked.")
    elif field.marked:
        field.marked = False
    else:
        field.marked = True


def test_field(field: board.Field) -> bool:
    if field.marked or not field.hidden:
        raise ValueError("Error: Only unmarked hidden fields can be tested.")
    elif field.mine:
        exploded = True
    else:
        exploded = False
        field.hidden = False  # TO DO unhide whole surrounding region
    return exploded


def test_if_won(minefield: board.Board) -> bool:
    unhidden_fields = 0
    for row in minefield.board:
        for field in row:
            if not field.hidden and not field.mine:
                unhidden_fields += 1
    return unhidden_fields == minefield.rows * minefield.columns - minefield.mines


def finish_game(minefield: board.Board, message: str) -> None:
    os.system("clear")
    minefield.unhide_all_fields()
    minefield.print_board()
    print(message)
    quit()


def do_turn(minefield: board.Board) -> None:
    os.system("clear")
    minefield.print_board()
    action = get_player_action(
        f"Choose action ([m]ark/unmark field as mine, [t]est field): ", ["m", "t"]
    )
    row, column = get_field_coordinates(minefield)
    exploded = False
    won = False
    try:
        if action == "t":
            exploded = test_field(minefield.board[row][column])
            won = test_if_won(minefield)
        elif action == "m":
            toggle_field_marked(minefield.board[row][column])
    except ValueError as error:
        print(error)
        time.sleep(3)
    else:
        if exploded:
            finish_game(minefield, "A mine has exploded! Game over...")
        if won:
            finish_game(minefield, "Congratulations, you won!")
