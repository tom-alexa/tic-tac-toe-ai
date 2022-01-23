from .terminal import print_board, print_winner, print_draw
from .artificial_inteligence import minimax


class Game:
    def __init__(self, players: dict):
        self.cross = {**players["cross"], **{"sign": "x"}}
        self.circle = {**players["circle"], **{"sign": "o"}}

        self.board = ["-"] * 9
        #self.board = ["x", "x", "o", "o", "o", "x", "-", "-", "-"]
        self.turn = 1

        self.running = False
        self.winner = None

    def run(self):
        self.running = True
        while self.running:
            current_player = self.get_current_player(self.turn, self.cross, self.circle)
            print_board(self.board, name=current_player["name"])

            move = self.get_move()
            self.make_move(self.board, move, current_player)

            if self.check_winner(self.board, current_player):
                self.running = False
                self.winner = self.get_current_player(self.turn, self.cross, self.circle)
                print_board(self.board)
                print_winner(self.winner["name"])
                continue

            if not self.get_possible_moves(self.board):
                print_board(self.board)
                print_draw()
                self.running = False

            self.turn = self.change_turn(self.turn)

    def get_move(self):
        current_player = self.get_current_player(self.turn, self.cross, self.circle)
        possible_moves = self.get_possible_moves(self.board)
        if current_player["ai"]:
            _, move = minimax(self.cross, self.circle, self.board[:], self.turn, self.get_current_player, self.get_possible_moves, self.make_move, self.check_winner)
            return move
        else:
            while True:
                move = input("Write your move (1-9): ")
                try:
                    move = int(move)
                    if move < 1 or move > 9:
                        raise ValueError
                    if move not in possible_moves:
                        raise ValueError
                    return move
                except ValueError:
                    continue

    @staticmethod
    def make_move(board, move, current_player):
        board[move - 1] = current_player["sign"]

    @staticmethod
    def get_possible_moves(board):
        return set(i + 1 for i, sign in enumerate(board) if sign =="-")

    @staticmethod
    def check_winner(board, current_player):
        sign = current_player["sign"]
        for i in range(3):
            if board[i * 3] == sign and board[i * 3 + 1] == sign and board[i * 3 + 2] == sign:
                return True
            elif board[i] == sign and board[3 + i] == sign and board[6 + i] == sign:
                return True
        if board[0] == sign and board[4] == sign and board[8] == sign:
            return True
        if board[2] == sign and board[4] == sign and board[6] == sign:
            return True
        return False

    @staticmethod
    def change_turn(turn):
        return turn * -1

    @staticmethod
    def get_current_player(turn, cross, circle):
        return cross if turn > 0 else circle
