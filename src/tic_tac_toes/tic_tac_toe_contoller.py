from src.tic_tac_toes.mode_of_game import Game
from src.tic_tac_toes.player import Player
from tic_tac_toe import TicTacToe

x_and_o = TicTacToe()
players: list = x_and_o.get_player()
player1: Player = players[0]
player2: Player = players[1]


def display_tic_tac_menu():
    return f"""
====================================
|First player: {player1.get_name()}
|Second Player: {player2.get_name()}
====================================    
    """


def register_player():
    first_player_name = input("Enter the first player name " + player1.get_symbol() + ": ")
    second_player_name = input("Enter the second player name " + player2.get_symbol() + ": ")
    player1.set_name(first_player_name)
    player2.set_name(second_player_name)
    print(display_tic_tac_menu())


def print_line():
    for count in range(25):
        print("=", end="")
    print()


def print_board():
    for count in range(0, len(x_and_o.get_board())):
        if count == 0 or count == 3 or count == 6:
            print()
            print_line()
        print(x_and_o.get_board()[count], end="\t")
        print("|", end=" ")
    print()


def winner():
    print("Game over")
    return x_and_o.get_winner().get_name()


def play_tic_tac_toe():
    while x_and_o.mode_of_game() == Game.CONTINUE.value:
        for count in range(2):
            print_board()
            condition = True
            catch_exception(condition, count)
            if x_and_o.mode_of_game() == Game.WIN.value or x_and_o.mode_of_game() == Game.DRAW.value:
                break
    if x_and_o.mode_of_game() == Game.WIN.value:
        print(winner())
    elif x_and_o.mode_of_game() == Game.DRAW.value:
        print("It is a draw come back next year")


def catch_exception(condition, count):
    while condition:
        try:
            move = int(input(players[count].get_name() + " Enter your move number from 1 to 9 :"))
            x_and_o.play(players[count], move)
            condition = False
        except ValueError as exception:
            print(exception)
