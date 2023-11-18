filler = " ."
field = [filler for x in range(9)]
player_x = ""
player_o = ""

#zmienia kolejność znaków jeśli użytkownik użył złą kolejność
def text_order(input_text):
    if input_text[1].isdigit():
        input_text = input_text[::-1]
    return input_text

#zwraca indeksy odpowiednie do wprowadzonego wiersza
def row(player_input):
    if player_input[1] == "a":
        index = [i for i in range(0, 3)]
        return(index)
    if player_input[1] == "b":
        index = [i for i in range(3, 6)]
        return(index)
    if player_input[1] == "c":
        index = [i for i in range(6, 9)]
        return(index)

#rysuje pole gry
def output(c):
    print(f"  1 2 3",
          f"A{c[0]}{c[1]}{c[2]}",
          f"B{c[3]}{c[4]}{c[5]}",
          f"C{c[6]}{c[7]}{c[8]}",
          sep="\n")

output(field)

#sprawdza czy jest jeszcze wolne miejsce na polu
def check_free_space(a):
    for i in a:
        if i == filler:
            return (True)

#sprawdza czy jest polączenie trzech tych samych symboli
def check_win(b):
    if b[0] == b[1] == b[2] != filler:
        return (True)
    elif b[3] == b[4] == b[5] != filler:
        return (True)
    elif b[6] == b[7] == b[8] != filler:
        return (True)
    elif b[0] == b[3] == b[6] != filler:
        return (True)
    elif b[1] == b[4] == b[7] != filler:
        return (True)
    elif b[2] == b[5] == b[8] != filler:
        return (True)
    elif b[0] == b[4] == b[8] != filler:
        return (True)
    elif b[6] == b[4] == b[2] != filler:
        return (True)
    else:
        return (False)

while check_free_space(field) and not check_win(field):
    player_x = text_order(input("type place for X").lower())
    if field[row(player_x)[int(player_x[0])-1]] == filler:
        pass
    else:
        while field[row(player_x)[int(player_x[0]) - 1]] != filler:
            player_x = text_order(input("type place for X").lower())
    field[row(player_x)[int(player_x[0]) - 1]] = " X"
    output(field)
    if not check_win(field) and not check_free_space(field):
        print("Remis")
        break
    if check_win(field):
        print("Player X win")
        break
    else:
        player_o = text_order(input("type place for O").lower())
        if field[row(player_o)[int(player_o[0]) - 1]] == filler:
            pass
        else:
            while field[row(player_o)[int(player_o[0]) - 1]] != filler:
                player_o = text_order(input("type place for O").lower())
        field[row(player_o)[int(player_o[0]) - 1]] = " O"
        output(field)
        if check_win(field):
            print("Player O win")
            break
        if not check_win(field) and not check_free_space(field):
            print("Remis")


