import unittest

import board


class TestBoard(unittest.TestCase):
    def test_field_defaults(self) -> None:
        field = board.Field()
        self.assertTrue(field.hidden)
        self.assertFalse(field.mine)
        self.assertIsNone(field.clue)
        self.assertFalse(field.marked)

    def test_field_with_arguments(self) -> None:
        field = board.Field(hidden=False, mine=True, clue=2, marked=True)
        self.assertFalse(field.hidden)
        self.assertTrue(field.mine)
        self.assertEqual(field.clue, 2)
        self.assertTrue(field.marked)

    def test_create_board_defaults(self) -> None:
        sample_board = board.Board()
        self.assertEqual(len(sample_board.board), 10)
        self.assertEqual(len(sample_board.board[0]), 10)
        self.assertEqual(sample_board.mines, 10)
        self.assertIsInstance(sample_board.board[0][0], board.Field)

        mines = 0
        for row in sample_board.board:
            for field in row:
                mines += field.mine
        self.assertEqual(mines, 10)


if __name__ == "__main__":
    unittest.main()
