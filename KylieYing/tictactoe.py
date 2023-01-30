import random
import os
import time


class Player:
    def __init__(self, letter):
        self.letter = letter
        self.move = None


    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def make_move(self, game):
        while not self.is_valid_move(game):
            self.move = int(input('Select a position [0:8]: '))
        game.board[self.move] = self.letter


    def is_valid_move(self, game):
        if self.move in game.available_positions:
            return True
        return False


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def make_move(self, game):
        self.move = random.choice(game.available_positions)
        game.board[self.move] = self.letter
        time.sleep(0.5)


class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.winner = None
        self.available_positions = [range(9)]


    def print_board(self):
        for i in range(len(self.board) // 3):
            print('|' + '|'.join(self.board[i * 3: i * 3 + 3]) + '|')
        

    @staticmethod
    def print_board_nums():
        print('|0|1|2|\n|3|4|5|\n|6|7|8|\n')


    def is_winner(self, player):
        row_ind = player.move // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all(spot == player.letter for spot in row):
            self.winner = player.letter

        column_ind = player.move % 3
        column = [self.board[column_ind + i * 3] for i in range(3)]
        if all(spot == player.letter for spot in column):
            self.winner = player.letter

        diagonal1 = [self.board[i] for i in (0, 4, 8)]
        diagonal2 = [self.board[i] for i in (2, 4, 6)]
        if all(spot == player.letter for spot in diagonal1) | all(spot == player.letter for spot in diagonal2):
            self.winner = player.letter


    def available_moves(self):
        self.available_positions = [i for i, spot in enumerate(self.board) if spot == ' ']


    def print_game_interface(self):
        os.system('clear')
        self.print_board_nums()
        self.print_board()
    

def play(game, x_player, o_player):
    current_player = x_player
    while not game.winner:
        game.available_moves()
        if len(game.available_positions) > 0:
            game.print_game_interface()
            current_player.make_move(game)
            game.is_winner(current_player)
            current_player = o_player if current_player == x_player else x_player
        else:
            break
        
    game.print_game_interface()
    if game.winner:
        print(f'Player {game.winner} won!')
    else:
        print('It is a tie.')


game = TicTacToe()
x_player = HumanPlayer('X')
o_player = RandomComputerPlayer('O')
play(game, x_player, o_player)
