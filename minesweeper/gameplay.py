import board

MIN_ROWS = 1
MAX_ROWS = 10
MIN_COLUMNS = 1
MAX_COLUMNS = 10


def get_board_parameter(message: str, minimum: int, maximum: int) -> int:
    while True:
        try:
            number = int(input(f"{message} ({minimum}-{maximum}): "))
            if not minimum <= number <= maximum:
                raise ValueError("Number not within limits!")
        except ValueError as error:
            print(f"Error: {error}")
        else:
            break
    return number


def get_action() -> str:
    pass


def create_board() -> board.Board:
    rows = get_board_parameter("Input the number of rows: ", MIN_ROWS, MAX_ROWS)
    columns = get_board_parameter(
        "Input the number of columns: ", MIN_COLUMNS, MAX_COLUMNS
    )
    mines = get_board_parameter("Input the number of mines: ", 1, rows * columns)
    return board.Board(rows, columns, mines)


def do_turn(minefield: board.Board) -> None:
    pass
