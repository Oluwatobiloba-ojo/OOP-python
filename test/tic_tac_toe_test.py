from unittest import TestCase

from src.tic_tac_toes import tic_tac_toe
from src.tic_tac_toes.exceptions.InvalidBox import InvalidBoxException
from src.tic_tac_toes.mode_of_game import Game
from src.tic_tac_toes.player import Player
from src.tic_tac_toes.tic_tac_toe_element import Tic_Tac_Element


class TestSomething(TestCase):
    def test_that_board_in_tic_tac_toe_is_set_to_empty(self):
        ticTacToe: tic_tac_toe = tic_tac_toe.TicTacToe()
        self.assertTrue(ticTacToe.isEmpty())

    def test_that_when_player_can_set_name_and_get_it(self):
        tic_tac = tic_tac_toe.TicTacToe()
        players: list = tic_tac.get_player()
        player1: Player = players[0]
        player1.set_name("tobi")
        self.assertEqual("tobi", player1.get_name())

    def test_that_when_players_can_set_there_names_and_get(self):
        x_and_0 = tic_tac_toe.TicTacToe()
        players: list = x_and_0.get_player()
        player1: Player = players[0]
        player2: Player = players[1]
        player2.set_name("ope")
        player1.set_name("yaya")
        self.assertEqual("ope", player2.get_name())
        self.assertEqual("yaya", player1.get_name())

    def test_that_player_can_mark_on_the_board_of_tic_tac_toe(self):
        x_and_o = tic_tac_toe.TicTacToe()
        players: list = x_and_o.get_player()
        player1: Player = players[0]
        x_and_o.mark_board(player1, 2)
        self.assertEqual(Tic_Tac_Element.X.value, x_and_o.get_board()[1])

    def test_that_two_players_can_not_play_in_the_same_direction_the_first_to_play_get_the_position(self):
        x_and_o = tic_tac_toe.TicTacToe()
        players: list = x_and_o.get_player()
        player1: Player = players[0]
        player2: Player = players[1]
        x_and_o.mark_board(player1, 2)
        with self.assertRaises(InvalidBoxException):
            x_and_o.mark_board(player2, 2)
        self.assertEqual(Tic_Tac_Element.X.value, x_and_o.get_board()[1])

    def test_that_player_can_play_tic_tac_toe_and_win_by_row_on_the_board(self):
        x_and_o = tic_tac_toe.TicTacToe()
        players: list = x_and_o.get_player()
        player1: Player = players[0]
        x_and_o.play(player1, 1)
        x_and_o.play(player1, 2)
        x_and_o.play(player1, 3)
        self.assertEqual(Game.WIN.value, x_and_o.mode_of_game())

    def test_that_when_two_player_plays_and_one_of_them_will_win_by_row(self):
        x_and_o = tic_tac_toe.TicTacToe()
        players: list = x_and_o.get_player()
        player1: Player = players[0]
        player2: Player = players[1]
        x_and_o.play(player1, 1)
        x_and_o.play(player1, 2)
        x_and_o.play(player1, 5)
        x_and_o.play(player2, 7)
        x_and_o.play(player2, 8)
        x_and_o.play(player2, 9)
        self.assertEqual(Game.WIN.value, x_and_o.mode_of_game())
        self.assertEqual(player2, x_and_o.get_winner())
        print(x_and_o.get_board())

    def test_that_player_can_win_through_column_of_the_box(self):
        x_and_o = tic_tac_toe.TicTacToe()
        players: list = x_and_o.get_player()
        player1: Player = players[0]
        x_and_o.play(player1, 1)
        x_and_o.play(player1, 4)
        x_and_o.play(player1, 7)
        self.assertEqual(Game.WIN.value, x_and_o.mode_of_game())
        self.assertEqual(player1, x_and_o.get_winner())

    def test_that_two_player_can_play_and_one_of_them_win_by_column(self):
        x_and_o = tic_tac_toe.TicTacToe()
        players: list = x_and_o.get_player()
        player1: Player = players[0]
        player2: Player = players[1]
        x_and_o.play(player1, 1)
        x_and_o.play(player1, 9)
        x_and_o.play(player1, 7)
        x_and_o.play(player2, 2)
        x_and_o.play(player2, 5)
        x_and_o.play(player2, 8)
        self.assertEqual(Game.WIN.value, x_and_o.mode_of_game())
        self.assertEqual(player2, x_and_o.get_winner())

    def test_that_player_can_win_diagonally_in_the_tic_tac_toe(self):
        x_and_o = tic_tac_toe.TicTacToe()
        players: list = x_and_o.get_player()
        player1: Player = players[0]
        player2: Player = players[1]
        x_and_o.play(player1, 1)
        x_and_o.play(player1, 5)
        x_and_o.play(player1, 9)
        self.assertEqual(Game.WIN.value, x_and_o.mode_of_game())
        self.assertEqual(player1, x_and_o.get_winner())

    def test_that_when_two_players_play_and_they_end_up_without_winning_it_is_a_draw(self):
        x_and_o = tic_tac_toe.TicTacToe()
        players: list = x_and_o.get_player()
        player1: Player = players[0]
        player2: Player = players[1]
        x_and_o.play(player1, 1)
        x_and_o.play(player1, 2)
        x_and_o.play(player1, 6)
        x_and_o.play(player1, 7)
        x_and_o.play(player1, -1)
        x_and_o.play(player2, 3)
        x_and_o.play(player2, 4)
        x_and_o.play(player2, 5)
        x_and_o.play(player2, 0)
        print(x_and_o.get_board())
        self.assertEqual(Game.DRAW.value, x_and_o.mode_of_game())

    


