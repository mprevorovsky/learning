import unittest
from unittest.mock import call, patch

import gameplay


class TestGameplay(unittest.TestCase):
    def test_get_board_parameter(self) -> None:
        with patch("builtins.input", side_effect="3"), patch(
            "builtins.print"
        ) as mock_print:
            number = gameplay._get_board_parameter("text", 1, 10)
            self.assertEqual(mock_print.mock_calls, [])
            self.assertEqual(number, 3)
        with patch("builtins.input", side_effect=["w", "30", "3"]), patch(
            "builtins.print"
        ) as mock_print:
            number = gameplay._get_board_parameter("text", 1, 10)
            self.assertEqual(
                mock_print.mock_calls,
                [
                    call("Error: invalid literal for int() with base 10: 'w'"),
                    call("Error: Number not within limits: '30'"),
                ],
            )
            self.assertEqual(number, 3)

    # def test_create_board(self) -> None:
    #     with patch("builtins.input", side_effect=["2", "3", "4"]):
    #         sample_board = gameplay.Gameplay(1, 10, 1, 10)
    #         self.assertEqual(sample_board.rows, 2)
    #         self.assertEqual(sample_board.columns, 3)
    #         mines = 0
    #         for row in sample_board.board:
    #             for field in row:
    #                 mines += field.mine
    #         self.assertEqual(mines, 4)


if __name__ == "__main__":
    unittest.main()
