"""Printing in terminal"""


def print_board(board: list[str], name: str = None) -> None:
    """Print board"""
    print()
    for row in range(3):
        for column in range(3):
            print(f"|{board[row * 3 + column]}", end="")
        print("|")
    if name:
        print(f"\nTurn: {name}", end="\n\n")


def print_winner(winner: str) -> None:
    """Print name of the winner"""
    print(f"\nWinner is {winner}\n")


def print_draw() -> None:
    """Print draw"""
    print("\nIt's a draw\n")
