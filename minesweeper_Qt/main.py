import sys
from dataclasses import dataclass

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

ROWS = 10
COLUMNS = 10
MINES = 10
TILE_SIZE = 50


@dataclass
class Field:
    hidden: bool = True
    mine: bool = False
    clue: int = 0
    marked: bool = False

    MINE_CHAR = "💣"
    EXPLODED_MINE_CHAR = "🔥"
    MARKED_CHAR = "❎"

    HIDDEN_TILE_ICON = "./images/tile_hidden.png"
    UNHIDDEN_TILE_ICON = "./images/tile_unhidden.png"

    def get_icon_representation(self) -> str:
        if self.hidden and self.marked:
            char = self.MARKED_CHAR
        elif not self.hidden and self.mine:
            char = self.MINE_CHAR
        elif not self.hidden and self.clue:
            char = str(self.clue)
        else:
            char = ""
        return char


class Board:
    def __init__(self, rows: int, columns: int, mines: int, tile_size: int) -> None:
        self.rows = rows
        self.columns = columns
        self.mines = mines
        self.tile_size = tile_size
        self.create_window()
        self.create_tiles()

    def create_window(self) -> None:
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.setGeometry(
            100,
            150,
            self.tile_size * self.rows + 50,
            self.tile_size * self.columns + 50,
        )
        self.window.setWindowTitle("Minesweeper")
        self.window.show()
        sys.exit(self.app.exec_())

    def create_tiles(self) -> None:
        self.label = QtWidgets.QLabel(self.window)
        self.label.move(50, 50)
        self.label.setPixmap(QtGui.QPixmap("./images/tile_hidden.png"))
        self.label.setText("test")
        self.label.adjustSize()


def main() -> None:
    game = Board(ROWS, COLUMNS, MINES, TILE_SIZE)
    game.label = QtWidgets.QLabel(game.window)
    game.label.move(50, 50)
    game.label.setPixmap(QtGui.QPixmap("./images/tile_hidden.png"))
    game.label.setText("test")
    game.label.adjustSize()


if __name__ == "__main__":
    main()
