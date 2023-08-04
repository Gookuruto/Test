import random

list_of_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def wordchoice():
    wordlist = ['drzewo', 'pies', 'wiosło', 'masło' ]
    global the_word
    the_word = random.choice(wordlist)   # losuje słowo
    print(the_word)
    word_lenght = len(the_word)          # określa długość ciągu znaków(wylosowanego słowa)
    print(word_lenght)
    global floor
    floor = ''
    for _ in range(word_lenght):         # tworzy podłoge z tylu znaków ile ma słowo
        floor += '_'
    print(floor)

def player_input():
        player_letter = input('Wpisz literkę: ')        # wczytuje literke od usera
        if player_letter in list_of_letters:            # jeśli literka jest w alfabecie; usuwa literke z alfabetu/listy -
            list_of_letters1 = list_of_letters.remove(player_letter)
            return player_letter        # - i zwraca literke wpisana
        else:
            print('źle')


def in_word():
    if player_input() in the_word:          # jeśli literka usera jest w haśle
        print_updated_floor()               # wyświetl nową podłoge z literką w odpowiednim miejscu
        print('tu jestem')                  # info dla mnie że kod tu doszedł
    else: print('nie ma tej litery - spróbuj ponownie')

def print_updated_floor():
    times_appears = the_word.count(player_input())
    letter_index = the_word.index(player_input())
    upd_floor = floor.replace(floor[letter_index], player_input(), 1)
    print(upd_floor)
    print(times_appears)
    print(letter_index)

def final_guess():
    print('jesli nie znasz wpisz N')
    guess = input('Jeśli znasz hasło - zgaduj: ')
    counter = 5
    if guess == "N":
        return None

    if guess == the_word:
        print('Wygrałeś')
        return True
    elif guess != the_word:
        counter -= 1
        print('złe hasło')
        print(f'pozostało {counter} szans')
        return None
    if counter < 1:
        print('Przegrałeś')
        return True


def launch_game():
    wordchoice()
    while final_guess() == None:
        try:
            in_word()
        except:
            print('coś poszło nie tak')
        finally:
            final_guess()

launch_game()