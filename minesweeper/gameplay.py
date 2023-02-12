import os
import time
from typing import Tuple

import board


def _get_board_parameter(message: str, minimum: int, maximum: int) -> int:
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


def _get_player_action(message: str, allowed_actions: list[str]) -> str:
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


class Gameplay:
    def __init__(
        self, min_rows: int, max_rows: int, min_columns: int, max_columns: int
    ) -> None:
        self.MIN_ROWS = min_rows
        self.MAX_ROWS = max_rows
        self.MIN_COLUMNS = min_columns
        self.MAX_COLUMNS = max_columns
        self.minefield = self._create_board()

    def _create_board(self) -> board.Board:
        rows = _get_board_parameter(
            f"Input the number of rows ({self.MIN_ROWS}, {self.MAX_ROWS}): ",
            self.MIN_ROWS,
            self.MAX_ROWS,
        )
        columns = _get_board_parameter(
            f"Input the number of columns ({self.MIN_COLUMNS}, {self.MAX_COLUMNS}): ",
            self.MIN_COLUMNS,
            self.MAX_COLUMNS,
        )
        mines = _get_board_parameter(
            f"Input the number of mines (1-{rows * columns}): ", 1, rows * columns
        )
        return board.Board(rows, columns, mines)

    def _get_field_coordinates(self) -> tuple[int, int]:
        row = _get_board_parameter(
            f"Select row (0-{self.minefield.rows - 1}): ",
            0,
            self.minefield.rows - 1,
        )
        column = _get_board_parameter(
            f"Select column (0-{self.minefield.columns - 1}): ",
            0,
            self.minefield.columns - 1,
        )
        return row, column

    def _test_if_won(self) -> bool:
        unhidden_fields = 0
        for row in self.minefield.board:
            for field in row:
                if not field.hidden:
                    unhidden_fields += 1
        return (
            unhidden_fields + self.minefield.mines
            == self.minefield.rows * self.minefield.columns
        )

    def _finish_game(self, message: str) -> None:
        os.system("clear")
        self.minefield.unhide_all_fields()
        self.minefield.print_board()
        print(message)
        quit()

    def do_turn(self) -> None:
        os.system("clear")
        self.minefield.print_board()
        action = _get_player_action(
            f"Choose action ([m]ark/unmark field as mine, [t]est field): ", ["m", "t"]
        )
        row, column = self._get_field_coordinates()
        exploded = False
        try:
            if action == "t":
                exploded = self.minefield.test_field(row, column)
            elif action == "m":
                self.minefield.toggle_field_marked(row, column)
        except ValueError as error:
            print(error)
            time.sleep(3)
        else:
            if exploded:
                self._finish_game(
                    f"A mine has exploded at {row},{column}! Game over..."
                )

            if self._test_if_won():
                self._finish_game("Congratulations, you won!")
