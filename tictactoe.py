from typing import List
import os

board_state = [" "] * 9


def draw(board_state: List):
    os.system('cls')
    print(f"{board_state[6]}|{board_state[7]}|{board_state[8]}")
    print("-------------")
    print(f"{board_state[3]}|{board_state[4]}|{board_state[5]}")
    print("-------------")
    print(f"{board_state[0]}|{board_state[1]}|{board_state[2]}")


def player_move(board_state: List, player_symbol: str):
    position = int(input("numer pola 1-9(jak na klawiaturze numerycznej): "))
    while board_state[position - 1] != " ":
        position = int(input("numer pola 1-9(jak na klawiaturze numerycznej): "))
    board_state[position - 1] = player_symbol


def check_win_condition(board_state: List) -> str:
    # Wiersze
    if board_state[0] == board_state[1] == board_state[2] and board_state[0] != " ":
        return f"Wygrał {board_state[0]}"
    if board_state[3] == board_state[4] == board_state[5] and board_state[3] != " ":
        return f"Wygrał {board_state[3]}"
    if board_state[6] == board_state[7] == board_state[8] and board_state[6] != " ":
        return f"Wygrał {board_state[6]}"

    # kolumny
    if board_state[0] == board_state[3] == board_state[6] and board_state[0] != " ":
        return f"Wygrał {board_state[0]}"
    if board_state[1] == board_state[4] == board_state[7] and board_state[1] != " ":
        return f"Wygrał {board_state[1]}"
    if board_state[2] == board_state[5] == board_state[8] and board_state[2] != " ":
        return f"Wygrał {board_state[2]}"

    # skosy
    if board_state[6] == board_state[4] == board_state[2] and board_state[2] != " ":
        return f"Wygrał {board_state[4]}"
    if board_state[8] == board_state[4] == board_state[0] and board_state[4] != " ":
        return f"Wygrał {board_state[4]}"

    #remis
    if all([state != " " for state in board_state]):
        return "Remis"

    return None


player_symbol = "o"
while True:
    draw(board_state)
    player_move(board_state, player_symbol)
    who_win = check_win_condition(board_state)
    if who_win is not None:
        draw(board_state)
        print(who_win)
        break
    if player_symbol == "o":
        player_symbol = "x"
    else:
        player_symbol = "o"
