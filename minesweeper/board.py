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

    def create_board(self) -> None:
        def place_mines(self) -> None:
            pass

        def place_clues(self) -> None:
            pass

    def print_board(self) -> None:
        pass

    def unhide_fields(self) -> None:
        pass
