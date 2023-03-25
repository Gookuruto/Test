"""
Koncepcja:
1. program wybiera losowo słowo z listy.
2. uzytkownik ma mozliwosc pomylenia sie 5 razy
3. uzytkownik podaje litery
    - jezeli litera jest w slowie to wypisywane jest z postaci np. __a_____
    - jezeli litera nie występuje to odejmowana jest 1 szansa (mozna rysować czlowieczka w konsoli)
4. gra konczy sie jak uzytkownik zgadnie słowo lub zmarnuje wszystkie szanse.
"""
import random


def repeat(word, character):
    l = []
    for i, w in enumerate(word):
        if w == character:
            l.append(i)
    return l


def guessing_letter(rletters, board, wrong):
    msg = input('Odgadnij literę: ')
    if msg in rletters:
        b = repeat(rletters, msg)
        for index in b:
            board[index] = msg
            rletters[index] = "$"
    else:
        wrong += 1
    return board, wrong


def check_win(board, wrong, stages, random_word, win):
    if '_' not in board:
        print("Gratulacje! Wygrałeś")
        print("".join(board))
        win = True
    if not win and wrong >= len(stages) - 1:
        print('Przegrałeś!')
        print(f' prawidłowa odpowiedź: {random_word}')


def hangman():
    random_words_list = ["rzeczy", 'inne', 'rozne', 'roznosci']
    random_word = random.choice(random_words_list).lower()

    wrong = 0
    stages = ["",
              "________        ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    rletters = list(random_word)
    board = ["_"] * len(random_word)
    win = False
    print("Gra w wisielca")
    while wrong < len(stages) - 1:
        board, wrong = guessing_letter(rletters, board, wrong)
        print(''.join(board))
        print('\n'.join(stages[0:wrong]))
        check_win(board, wrong, stages, random, win)


hangman()
