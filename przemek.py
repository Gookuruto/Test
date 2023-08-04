import random

def create_board():
    return [['O' for _ in range(10)] for _ in range(10)]

def print_board(board):
    print("  1 2 3 4 5 6 7 8 9 10")
    for i, row in enumerate(board):
        print(chr(65 + i) + ' ' + ' '.join(row))

def place_ships(board):
    ships = [(5, "Carrier")]
    for ship_length, ship_name in ships:
        while True:
            try:
                print_board(board)
                print(f"Placing {ship_name} ({ship_length} cells)")
                row = int(input("Enter the row (1-10): ")) - 1
                col = int(input("Enter the column (1-10): ")) - 1
                orientation = input("Enter orientation (H for horizontal, V for vertical): ").upper()

                if orientation == 'H':
                    if col + ship_length <= 10 and all(board[row][col+i] == 'O' for i in range(ship_length)):
                        for i in range(ship_length):
                            board[row][col + i] = 'S'
                        break
                elif orientation == 'V':
                    if row + ship_length <= 10 and all(board[row+i][col] == 'O' for i in range(ship_length)):
                        for i in range(ship_length):
                            board[row + i][col] = 'S'
                        break

                print("Invalid placement. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

def get_guess():
    while True:
        try:
            guess = input("Enter your guess (e.g., A1): ").upper()
            row = ord(guess[0]) - 65
            col = int(guess[1:]) - 1
            return row, col
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def check_hit(board, row, col):
    if board[row][col] == 'S':
        print("Hit!")
        board[row][col] = 'X'
        return True
    elif board[row][col] == 'O':
        print("Miss!")
        board[row][col] = '/'
    else:
        print("You've already guessed this location.")
    return False

def is_game_over(board):
    return all(all(cell != 'S' for cell in row) for row in board)

def main():
    print("Welcome to Battleship Game!")
    board = create_board()
    place_ships(board)
    enemy_board = create_board()
    place_ships(enemy_board)

    current_board = create_board()
    while not is_game_over(board) and not is_game_over(enemy_board):
        print("Your Board:")
        print_board(current_board)

        print("\nEnemy's Board:")
        print_board(board)

        print("\nYour Turn:")
        row, col = get_guess()
        check_hit(board, row, col)

        print("\nEnemy's Turn:")
        enemy_row, enemy_col = get_guess()
        enemy_row, enemy_col = random.randint(0, 9), random.randint(0, 9)
        check_hit(current_board, enemy_row, enemy_col)

    if is_game_over(board):
        print("Congratulations! You sunk all the enemy ships!")
    else:
        print("Game Over. The enemy sunk all your ships!")

if __name__ == "__main__":
    main()