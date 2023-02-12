import os

import gameplay

MIN_ROWS = 2
MAX_ROWS = 10
MIN_COLUMNS = 2
MAX_COLUMNS = 10


def main() -> None:
    os.system("clear")
    print("Welcome to the Minesweeper game!")
    minesweeper = gameplay.Gameplay(MIN_ROWS, MAX_ROWS, MIN_COLUMNS, MAX_COLUMNS)
    while True:
        minesweeper.do_turn()


if __name__ == "__main__":
    main()
