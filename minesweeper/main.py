import gameplay


def main() -> None:
    print("Welcome to the Minesweeper game!")
    minefield = gameplay.create_board()
    minefield.print_board()


main()
