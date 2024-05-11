import copy
import itertools

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_player_counter = 0
    o_player_counter = 0
    for i, j in itertools.product(range(len(board)), range(len(board[0]))):
        if board[i][j] == 'X':
            x_player_counter += 1
        elif board[i][j] == 'O':
            o_player_counter += 1
    if x_player_counter > o_player_counter:
        return O
    return X

def actions(board):
    possible_actions = set()
    for i, j in itertools.product(range(len(board)), range(len(board[0]))):
        if board[i][j] == EMPTY:
            possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    if action not in actions(board):
        raise Exception('Invalid action!')
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)
    return board_copy

def winner(board):
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            if board[i][0] == 'X':
                return X
            elif board[i][0] == 'O':
                return O
            else:
                return None
    for i in range(len(board)):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            if board[0][i] == 'X':
                return X
            elif board[0][i] == 'O':
                return O
            else:
                return None
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        if board[0][0] == 'X':
            return X
        elif board[0][0] == 'O':
            return O
        else:
            return None
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        if board[0][2] == 'X':
            return X
        elif board[0][2] == 'O':
            return O
        else:
            return None
    return None


def terminal(board):
    if winner(board) is not None or not any(None in row for row in board):
        return True
    return False

def utility(board):
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

def minimax(board):
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board, float('-inf'), float('inf'))
            return move
        else:
            value, move = min_value(board, float('-inf'), float('inf'))
            return move

def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board), None
    perfect_move = tuple()
    v = float('inf')
    for action in actions(board):
        val, act = max_value(result(board, action), alpha, beta)
        if val < v:
            v = val
            perfect_move = action
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v, perfect_move

def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board), None
    perfect_move = tuple()
    v = float('-inf')
    for action in actions(board):
        val, act = min_value(result(board, action), alpha, beta)
        if val > v:
            v = val
            perfect_move = action
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v, perfect_move