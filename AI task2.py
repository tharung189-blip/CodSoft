import random

board = [" " for _ in range(9)]

# Display board
def show():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()

# Check win
def win(player):
    combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a]==board[b]==board[c]==player for a,b,c in combos)

# Get empty positions
def empty_positions():
    return [i for i in range(9) if board[i] == " "]

# AI Strategy (NOT Minimax - unique logic)
def ai_move():
    print("🤖 AI thinking strategically...\n")

    # 1. Win if possible
    for i in empty_positions():
        board[i] = "O"
        if win("O"):
            print(f"AI wins by placing at {i+1}")
            return
        board[i] = " "

    # 2. Block player win
    for i in empty_positions():
        board[i] = "X"
        if win("X"):
            board[i] = "O"
            print(f"AI blocks at {i+1}")
            return
        board[i] = " "

    # 3. Take center
    if 4 in empty_positions():
        board[4] = "O"
        print("AI takes center")
        return

    # 4. Take corners
    corners = [i for i in [0,2,6,8] if i in empty_positions()]
    if corners:
        move = random.choice(corners)
        board[move] = "O"
        print(f"AI takes corner {move+1}")
        return

    # 5. Take any remaining spot
    move = random.choice(empty_positions())
    board[move] = "O"
    print(f"AI moves at {move+1}")

# Player move
def player_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if pos in empty_positions():
                board[pos] = "X"
                break
            else:
                print("❌ Invalid move!")
        except:
            print("Enter valid number!")

# Game loop
def play():
    print("🔥 Strategic Tic-Tac-Toe AI")
    print("You = X | AI = O")
    print("Positions:\n1|2|3\n4|5|6\n7|8|9")

    while True:
        show()
        player_move()

        if win("X"):
            show()
            print("🎉 You Win!")
            break

        if not empty_positions():
            show()
            print("🤝 Draw!")
            break

        ai_move()

        if win("O"):
            show()
            print("🤖 AI Wins!")
            break

        if not empty_positions():
            show()
            print("🤝 Draw!")
            break

play()2
