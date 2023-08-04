# from typing import List
# import os
#
#
# def draw(stan_gry: List):
#     os.system('cls')
#     print(f"{stan_gry[6]}|{stan_gry[7]}|{stan_gry[8]}")
#     print("--------")
#     print(f"{stan_gry[3]}|{stan_gry[4]}|{stan_gry[5]}")
#     print("--------")
#     print(f"{stan_gry[0]}|{stan_gry[1]}|{stan_gry[2]}")
#
# def player_move(stan_gry: List, player_symbol: str):
#     pass
#
# def check_win_conditions(stan_gry: List) -> str:
#     if kolko wygra:
#         return "o"
#     if x wygra:
#         return "x"
#     if remis:
#         return "remis"
#     else:
#         return None
#
# board_state = [" "]*9
# symbol = "o"
# while True:
#     draw(board_state)
#     player_move(board_state)
#     if check_win_conditions() is not None:
#         print(check_win_conditions())
#         break
#     if symbol == "o":
#         symbol = "x"
#     else:
#         symbol = "o"


gues = "_"*4
print(str(gues))
guess = list(gues)[2] = 'w'
print("".join(guess))