"""
Napisz gre w kolko i krzyszyk. kroki:
1. stworz funkcje(klase) odpowiedzialną za plansze czyli za jej rysowanie zgodnie z obecnym stanem gry.
2. stworz funkcje ktora bedzie sprawdzać czy ktorys z graczy wygrał.
3. napisz kod ktory pozwoli graczom wykonywac swoj ruch na zmiane (trzeba zabronic nadpisywania ruchów)
4. Czy stworzony kod można jakos ulepszyć? zamknac w klasy jezeli chclielbysmy miec wiecej instancji naszej gry?
"""
import os
from typing import List


def draw_board(values_list: List[str]):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{values_list[7]}|{values_list[8]} |{values_list[9]} ")
    print("------")
    print(f"{values_list[4]}|{values_list[5]} |{values_list[6]} ")
    print("------")
    print(f"{values_list[1]}|{values_list[2]} |{values_list[3]} ")


def win_rule(values_list: List[str]) -> str:
    if values_list[1] == values_list[2] == values_list[3] and values_list[1] != " ":
        return values_list[1]
    elif values_list[4] == values_list[5] == values_list[6] and values_list[4] != " ":
        return values_list[4]
    elif values_list[7] == values_list[8] == values_list[9] and values_list[7] != " ":
        return values_list[7]
    else:
        return "undefined"


def player_move(player_icon, values_list) -> List[str]:
    field_number = int(input("Podaj pole 1-9: "))
    while values_list[field_number] != " ":
        field_number = int(input("Podaj pole 1-9: "))
    values_list[field_number] = player_icon
    return values_list


def change_icon(icon):
    if icon == 'o':
        return 'x'
    else:
        return 'o'


def game():
    playing_filed = [" "] * 10
    draw_board(playing_filed)
    player_icon = 'o'
    while True:
        player_move(player_icon, playing_filed)
        draw_board(playing_filed)
        player_icon = change_icon(player_icon)
        if win_rule(playing_filed) != "undefined":
            print(f"{win_rule(playing_filed)} has won")
            break


game()