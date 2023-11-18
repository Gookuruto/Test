import functions_storage as fs


def draw_board(*args):
    print("Kupa")


def main():
    game_field = [" "] * 9
    player_icon = "o"
    fs.draw_board(game_field)
    while not fs.end_condition_check(game_field):
        print(f"Ruch gracza {player_icon}")
        player_position = fs.player_input(game_field)
        game_field[player_position] = player_icon
        fs.draw_board(game_field)
        print("Round ended.")
        player_icon = "x" if player_icon == "o" else "o"

main()
