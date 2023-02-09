import unittest
from unittest.mock import call, patch

import board


class TestBoard(unittest.TestCase):
    def test_field_defaults(self) -> None:
        field = board.Field()
        self.assertTrue(field.hidden)
        self.assertFalse(field.mine)
        self.assertEqual(field.clue, 0)
        self.assertFalse(field.marked)

    def test_field_with_arguments(self) -> None:
        field = board.Field(hidden=False, mine=True, clue=2, marked=True)
        self.assertFalse(field.hidden)
        self.assertTrue(field.mine)
        self.assertEqual(field.clue, 2)
        self.assertTrue(field.marked)

    def test_field_printing_representation(self) -> None:
        field = board.Field()
        self.assertEqual(field.get_printing_representation(), "█")
        field = board.Field(hidden=False)
        self.assertEqual(field.get_printing_representation(), " ")
        field = board.Field(marked=True)
        self.assertEqual(field.get_printing_representation(), "\033[93mM\033[0m")
        field = board.Field(hidden=False, clue=1)
        self.assertEqual(field.get_printing_representation(), "\033[92m1\033[0m")
        field = board.Field(hidden=False, mine=True)
        self.assertEqual(field.get_printing_representation(), "\033[91mX\033[0m")

    def test_create_board_defaults(self) -> None:
        sample_board = board.Board()
        self.assertEqual(len(sample_board.board), 10)
        self.assertEqual(len(sample_board.board[0]), 10)
        self.assertEqual(sample_board.mines, 10)
        self.assertIsInstance(sample_board.board[0][0], board.Field)

        mines = 0
        hidden = 0
        marked = 0
        for row in sample_board.board:
            for field in row:
                mines += field.mine
                hidden += field.hidden
                marked += field.marked
        self.assertEqual(mines, 10)
        self.assertEqual(hidden, 100)
        self.assertEqual(marked, 0)

    def test_create_board_with_arguments(self) -> None:
        row_number = 12
        column_number = 4
        mine_number = 3
        sample_board = board.Board(
            rows=row_number, columns=column_number, mines=mine_number
        )
        self.assertEqual(len(sample_board.board), row_number)
        self.assertEqual(len(sample_board.board[0]), column_number)
        self.assertEqual(sample_board.mines, mine_number)

        mines = 0
        hidden = 0
        for row in sample_board.board:
            for field in row:
                mines += field.mine
                hidden += field.hidden
        self.assertEqual(mines, mine_number)
        self.assertEqual(hidden, row_number * column_number)

    def test_unhide_fields(self) -> None:
        sample_board = board.Board(rows=5, columns=5)
        sample_board.unhide_fields()
        hidden = 0
        for row in sample_board.board:
            for field in row:
                hidden += field.hidden
        self.assertEqual(hidden, 0)

    def test_mine_clue_placement(self) -> None:
        # mines
        #   012
        # 0 M__
        # 1 __M
        # 2 ___

        rows = 3
        columns = 3
        expected_clues = [[0, 2, 1], [1, 2, 0], [0, 1, 1]]
        sample_board = board.Board(rows=rows, columns=columns, mines=0)
        sample_board.board[0][0].mine = True
        sample_board.board[1][2].mine = True
        sample_board._place_clues()
        clues = []
        for row in range(rows):
            row_clues = []
            for column in range(columns):
                row_clues.append(sample_board.board[row][column].clue)
            clues.append(row_clues)
        self.assertEqual(clues, expected_clues)

    @patch("board.print")
    def test_print_board(self, mock_print) -> None:
        sample_board = board.Board(rows=1, columns=1, mines=0)
        sample_board.print_board()
        self.assertEqual(
            mock_print.mock_calls,
            [
                call(" |", end=""),
                call("0|", end=""),
                call(),
                call("0|", end=""),
                call("█|", end=""),
                call(),
            ],
        )


if __name__ == "__main__":
    unittest.main()
