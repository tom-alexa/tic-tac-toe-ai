import random

def minimax(cross, circle, board, turn, get_current_player, get_possible_moves, make_move, check_winner, depth=9):
    possible_moves = get_possible_moves(board)
    current_player = get_current_player(turn, cross, circle)
    best_score = None
    best_moves = []
    for move in possible_moves:
        new_board = board[:]
        make_move(new_board, move, current_player)

        if check_winner(new_board, current_player):
            return turn, move

        if not get_possible_moves(new_board):
            return 0, move

        score, _ = minimax(cross, circle, new_board, turn * -1, get_current_player, get_possible_moves, make_move, check_winner)
        if best_score == None:
            best_score = score
        if score == best_score:
            best_moves.append(move)
        if (turn > 0 and score > best_score) or (turn < 0 and score < best_score):
            best_score = score
            best_moves = [move]

    return best_score, random.choice(best_moves)
