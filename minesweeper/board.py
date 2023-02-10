import itertools
import random
from dataclasses import dataclass


@dataclass
class Field:
    hidden: bool = True
    mine: bool = False
    clue: int = 0
    marked: bool = False

    HIDDEN_CHAR = "█"
    MINE_CHAR = "\033[91m" + "X" + "\033[0m"
    EXPLODED_MINE_CHAR = "\033[91m" + "X" + "\033[0m"
    MARKED_CHAR = "\033[93m" + "M" + "\033[0m"
    EMPTY_CHAR = " "

    def get_printing_representation(self) -> str:
        if self.hidden and self.marked:
            char = self.MARKED_CHAR
        elif self.hidden and not self.marked:
            char = self.HIDDEN_CHAR
        elif not self.hidden and self.mine:
            char = self.MINE_CHAR
        elif not self.hidden and self.clue:
            char = "\033[92m" + str(self.clue) + "\033[0m"
        else:
            char = self.EMPTY_CHAR
        return char


class Board:
    def __init__(self, rows: int = 10, columns: int = 10, mines: int = 10) -> None:
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.board = []
        self._create_board_fields()
        self._place_mines()
        self._place_clues()

    def _create_board_fields(self) -> None:
        for _ in range(self.rows):
            row = []
            for _ in range(self.columns):
                row.append(Field())
            self.board.append(row)

    def _place_mines(self) -> None:
        all_field_coordinates = tuple(
            itertools.product(range(self.rows), range(self.columns))
        )
        for row, column in random.sample(all_field_coordinates, k=self.mines):
            self.board[row][column].mine = True

    def _place_clues(self) -> None:
        mine_fields = []
        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[row][column].mine:
                    mine_fields.append([row, column])

        for row, column in mine_fields:
            neighbor_fields = [
                [row - 1, column - 1],
                [row - 1, column],
                [row - 1, column + 1],
                [row, column - 1],
                [row, column + 1],
                [row + 1, column - 1],
                [row + 1, column],
                [row + 1, column + 1],
            ]
            for field in neighbor_fields:
                if field[0] in range(self.rows) and field[1] in range(self.columns):
                    self.board[field[0]][field[1]].clue += 1

    def print_board(self) -> None:
        print(" |", end="")
        for j in range(self.columns):
            print(f"{j}|", end="")
        print()
        for i in range(self.rows):
            print(f"{i}|", end="")
            for j in range(self.columns):
                print(f"{self.board[i][j].get_printing_representation()}|", end="")
            print()

    def _unhide_field(self, row: int, column: int) -> None:
        self.board[row][column].hidden = False

    def unhide_all_fields(self) -> None:
        for row in range(self.rows):
            for column in range(self.columns):
                self._unhide_field(row, column)

    def toggle_field_marked(self, row: int, column: int) -> None:
        field = self.board[row][column]
        if not field.hidden:
            raise ValueError("Error: Only hidden fields may be (un)marked.")
        elif field.marked:
            field.marked = False
        else:
            field.marked = True

    def test_field(self, row: int, column: int) -> bool:
        field = self.board[row][column]
        if field.marked or not field.hidden:
            raise ValueError("Error: Only unmarked hidden fields can be tested.")
        elif field.mine:
            exploded = True
        else:
            exploded = False
            field.hidden = False  # TO DO unhide whole surrounding region
        return exploded
