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

    def _get_neighbor_positions(self, row: int, column: int) -> list[list[int]]:
        all_neighbor_positions = [
            [row - 1, column - 1],
            [row - 1, column],
            [row - 1, column + 1],
            [row, column - 1],
            [row, column + 1],
            [row + 1, column - 1],
            [row + 1, column],
            [row + 1, column + 1],
        ]
        valid_neighbor_positions = []
        for neighbor_row, neighbor_column in all_neighbor_positions:
            if neighbor_row in range(self.rows) and neighbor_column in range(
                self.columns
            ):
                valid_neighbor_positions.append([neighbor_row, neighbor_column])

        return valid_neighbor_positions

    def _place_clues(self) -> None:
        mine_positions = []
        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[row][column].mine:
                    mine_positions.append([row, column])

        for row, column in mine_positions:
            neighbor_positions = self._get_neighbor_positions(row, column)
            for neighbor_row, neighbor_column in neighbor_positions:
                self.board[neighbor_row][neighbor_column].clue += 1

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

    def _unhide_neighbor_fields(self, row: int, column: int) -> None:
        neighbor_positions = self._get_neighbor_positions(row, column)
        for neighbor_row, neighbor_column in neighbor_positions:
            if (
                self.board[neighbor_row][neighbor_column].hidden
                and self.board[neighbor_row][neighbor_column].clue > 0
                and not self.board[neighbor_row][neighbor_column].mine
            ):
                self.board[neighbor_row][neighbor_column].hidden = False
            elif (
                self.board[neighbor_row][neighbor_column].hidden
                and self.board[neighbor_row][neighbor_column].clue == 0
                and not self.board[neighbor_row][neighbor_column].mine
            ):
                self.board[neighbor_row][neighbor_column].hidden = False
                self._unhide_neighbor_fields(neighbor_row, neighbor_column)

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
            field.hidden = False
            self._unhide_neighbor_fields(row, column)
        return exploded
