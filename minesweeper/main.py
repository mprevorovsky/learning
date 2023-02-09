import os

import gameplay


def main() -> None:
    os.system("clear")
    print("Welcome to the Minesweeper game!")
    minefield = gameplay.create_board()
    while True:
        gameplay.do_turn(minefield)


main()
