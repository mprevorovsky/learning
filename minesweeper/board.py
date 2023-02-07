import itertools
import random
from dataclasses import dataclass


@dataclass
class Field:
    hidden: bool = True
    mine: bool = False
    clue: int | None = None
    marked: bool = False


class Board:
    def __init__(self, rows: int = 10, columns: int = 10, mines: int = 10) -> None:
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.board = []
        self._create_board()

    def _place_mines(self) -> None:
        all_field_coordinates = tuple(
            itertools.product(range(self.rows), range(self.columns))
        )
        for row, column in random.sample(all_field_coordinates, k=self.mines):
            self.board[row][column].mine = True

    def _place_clues(self) -> None:
        pass

    def _create_board_fields(self) -> None:
        for _ in range(self.rows):
            row = []
            for _ in range(self.columns):
                row.append(Field())
            self.board.append(row)

    def _create_board(self) -> None:
        self._create_board_fields()
        self._place_mines()
        self._place_clues()

    def print_board(self) -> None:
        pass

    def unhide_fields(self) -> None:
        pass
