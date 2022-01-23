
def print_board(board, name=None):
    print()
    for row in range(3):
        for column in range(3):
            print(f"|{board[row * 3 + column]}", end="")
        print("|")
    if name:
        print(f"\nTurn: {name}", end="\n\n")


def print_winner(winner):
    print(f"Winner is {winner}\n")

def print_draw():
    print("It's a draw\n")