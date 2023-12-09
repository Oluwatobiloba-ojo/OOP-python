from src.tic_tac_toes import player
from src.tic_tac_toes.exceptions.InvalidBox import InvalidBoxException
from src.tic_tac_toes.mode_of_game import Game
from src.tic_tac_toes.player import Player
from src.tic_tac_toes.tic_tac_toe_element import Tic_Tac_Element


class TicTacToe:
    def __init__(self):
        self._board = []
        self._isEmpty = True
        self._mode_of_game: Game = Game.CONTINUE.value
        self._winner = None
        self._players: list = [Player(Tic_Tac_Element.X.value), Player(Tic_Tac_Element.O.value)]
        for i in range(3):
            for j in range(3):
                self._board.append(Tic_Tac_Element.EMPTY.value)

    def isEmpty(self) -> bool:
        for value in self._board:
            if value is not Tic_Tac_Element.EMPTY.value:
                self._isEmpty = False
                break
        return self._isEmpty

    def get_player(self):
        return self._players

    def mark_board(self, players: player.Player, move: int):
        if self._board[move-1] == Tic_Tac_Element.EMPTY.value:
            self._board[move-1] = players.get_symbol()
        else:
            raise InvalidBoxException("Box already filled")

    def get_board(self):
        return self._board

    def _check_row(self, players: Player):
        if players.get_symbol() == self._board[0] and players.get_symbol() == self._board[1] and players.get_symbol() == \
                self._board[2]:
            return True
        elif players.get_symbol() == self._board[3] and players.get_symbol() == self._board[
            4] and players.get_symbol() == \
                self._board[5]:
            return True
        elif players.get_symbol() == self._board[6] and players.get_symbol() == self._board[
            7] and players.get_symbol() == \
                self._board[8]:
            return True

    def play(self, players, move):
        self.mark_board(players, move)
        self._mode_of_game = self._check(players)
        if self._mode_of_game == Game.WIN.value:
            self._mode_of_game = Game.WIN.value
            self._winner = players

    def mode_of_game(self):
        return self._mode_of_game

    def get_winner(self):
        return self._winner

    def _check(self, players):
        if self._check_row(players):
            return Game.WIN.value
        elif self._check_column(players):
            return Game.WIN.value
        elif self._check_diagonally(players):
            return Game.WIN.value
        elif self._isFull():
            return Game.DRAW.value
        else:
            return Game.CONTINUE.value

    def _check_column(self, players: Player):
        if players.get_symbol() == self._board[0] and players.get_symbol() == self._board[3] and players.get_symbol() == \
                self._board[6]:
            return True
        elif players.get_symbol() == self._board[1] and players.get_symbol() == self._board[
            4] and players.get_symbol() == \
                self._board[7]:
            return True
        elif players.get_symbol() == self._board[2] and players.get_symbol() == self._board[
            5] and players.get_symbol() == \
                self._board[8]:
            return True

    def _check_diagonally(self, players):
        if players.get_symbol() == self._board[0] and players.get_symbol() == self._board[4] and players.get_symbol() == \
                self._board[8]:
            return True
        elif players.get_symbol() == self._board[2] and players.get_symbol() == self._board[4] and players.get_symbol() ==\
                self._board[6]:
            return True

    def _isFull(self):
        for count in self._board:
            if count == Tic_Tac_Element.EMPTY.value: return False
        return True
