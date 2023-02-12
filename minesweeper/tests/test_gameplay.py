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

    def test_get_player_action(self) -> None:
        with patch("builtins.input", side_effect=["1", "t", "b"]), patch(
            "builtins.print"
        ) as mock_print:
            action = gameplay._get_player_action("text", ["a", "b"])
            self.assertEqual(
                mock_print.mock_calls,
                [
                    call("Error: Incorrect input: 1"),
                    call("Error: Incorrect input: t"),
                ],
            )
            self.assertEqual(action, "b")

    def test_get_field_coordinates(self) -> None:
        with patch("builtins.input", side_effect=["2", "2", "1"]):
            sample_game = gameplay.Gameplay(1, 10, 1, 10)
        with patch("builtins.input", side_effect=["1", "w", "20", "1"]), patch(
            "builtins.print"
        ) as mock_print:
            row, column = sample_game._get_field_coordinates()
            self.assertEqual((row, column), (1, 1))
            self.assertEqual(
                mock_print.mock_calls,
                [
                    call("Error: invalid literal for int() with base 10: 'w'"),
                    call("Error: Number not within limits: '20'"),
                ],
            )

    def test_create_board(self) -> None:
        with patch("builtins.input", side_effect=["2", "3", "4"]):
            sample_game = gameplay.Gameplay(1, 10, 1, 10)
            self.assertEqual(sample_game.minefield.rows, 2)
            self.assertEqual(sample_game.minefield.columns, 3)
            mines = 0
            for row in sample_game.minefield.board:
                for field in row:
                    mines += field.mine
            self.assertEqual(mines, 4)

    def test_finish_game(self) -> None:
        with patch("builtins.input", side_effect=["1", "1", "1"]):
            sample_game = gameplay.Gameplay(1, 10, 1, 10)
        with patch("builtins.print") as mock_print, patch("builtins.quit") as mock_quit:
            sample_game._finish_game("text")
            self.assertEqual(
                mock_print.mock_calls,
                [
                    call(" |", end=""),
                    call("0|", end=""),
                    call(),
                    call("0|", end=""),
                    call("\033[91mX\033[0m|", end=""),
                    call(),
                    call("text"),
                ],
            )
            assert mock_quit.called

    def test_test_if_won(self) -> None:
        with patch("builtins.input", side_effect=["2", "2", "1"]):
            sample_game = gameplay.Gameplay(1, 10, 1, 10)
            sample_game.minefield.board[0][0].mine = False
            sample_game.minefield.board[0][1].mine = False
            sample_game.minefield.board[1][0].mine = False
            sample_game.minefield.board[1][1].mine = True
        self.assertFalse(sample_game._test_if_won())
        sample_game.minefield.board[1][1].marked = True
        self.assertFalse(sample_game._test_if_won())
        sample_game.minefield.board[0][0].hidden = False
        sample_game.minefield.board[0][1].hidden = False
        sample_game.minefield.board[1][0].hidden = False
        self.assertTrue(sample_game._test_if_won())
        sample_game.minefield.board[1][1].marked = False
        self.assertTrue(sample_game._test_if_won())

    def test_do_turn(self) -> None:
        with patch("builtins.input", side_effect=["1", "1", "1"]):
            sample_game = gameplay.Gameplay(1, 10, 1, 10)
        with patch("builtins.input", side_effect=["t", "0", "0"]), patch(
            "builtins.quit"
        ) as mock_quit, patch("board.Board.test_field") as mock_test_field:
            sample_game.do_turn()
            assert mock_test_field.called
            assert mock_quit.called

        with patch("builtins.input", side_effect=["2", "2", "1"]):
            sample_game = gameplay.Gameplay(1, 10, 1, 10)
        sample_game.minefield.board[0][0].hidden = False
        with patch("builtins.input", side_effect=["m", "0", "0"]), patch(
            "builtins.print"
        ):
            sample_game.do_turn()

        with patch("builtins.input", side_effect=["1", "1", "1"]):
            sample_game = gameplay.Gameplay(1, 10, 1, 10)
        with patch("builtins.input", side_effect=["m", "0", "0"]), patch(
            "builtins.quit"
        ) as mock_quit, patch("board.Board.toggle_field_marked") as mock_marked, patch(
            "builtins.print"
        ):
            sample_game.do_turn()
            assert mock_marked.called
            assert mock_quit.called


if __name__ == "__main__":
    unittest.main()
