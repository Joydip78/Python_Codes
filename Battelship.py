import random

# Constants
BOARD_SIZE = 6
NUM_SHIPS = 4
MAX_TURNS = 9

# Initialize board
def create_board():
    return [["~" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Print board nicely
def print_board(board, hide_ships=False):
    print("  " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        display_row = []
        for cell in row:
            if hide_ships and cell == "S":
                display_row.append("~")
            else:
                display_row.append(cell)
        print(f"{i} " + " ".join(display_row))

# Place ships randomly
def place_ships():
    board = create_board()
    c = 0
    while c < NUM_SHIPS:
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)
        if board[row][col] != "S":
            board[row][col] = "S"
            c += 1
    return board

# Main game loop
def play_game():
    print("🎯 Welcome to Battleship!")
    print(f"Try to sink all {NUM_SHIPS} enemy ships in {MAX_TURNS} turns!\n")

    board = create_board()
    hidden_board = place_ships()

    turns = 0
    hits = 0

    while turns <= MAX_TURNS and hits < NUM_SHIPS:
        print_board(board)
        try:
            row = int(input("\nEnter row (0–4): "))
            col = int(input("Enter column (0–4): "))

            if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
                print("⚠️ Invalid input. Provided Coordinate is out of range.")
                continue

            if board[row][col] in ["X", "O"]:
                print("🔁 You already guessed that spot!")
                continue

            turns += 1

            if hidden_board[row][col] == "S":
                print("💥 Hit!")
                board[row][col] = "X"
                hits += 1
            else:
                print("🌊 Miss.")
                board[row][col] = "O"

            print(f"Turns left: {MAX_TURNS - turns}")
            print(f"Hits: {hits}/{NUM_SHIPS}\n")

        except ValueError:
            print("❗ Please enter valid integers only.")
            continue

    if hits == NUM_SHIPS:
        print("🏆 Congratulations! You sank all the ships!")
    else:
        print("💀 Game Over. Better luck next time!")
        print("Here were the ships:")
        print_board(hidden_board)

# Run the game
if __name__ == "__main__":
    play_game()
