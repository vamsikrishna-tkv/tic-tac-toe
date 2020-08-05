"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    else:
        countX = 0
        countO = 0
        for row in board:
            for each in row:
                if each == X:
                    countX += 1
                    # print("countX")
                    # print(countX)
                elif each == O:
                    countO += 1
                    # print("counto")
                    # print(countO)
        if countO < countX:
            return O
        else:
            return X

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    setofactions = set()
    actionBoard = initial_state()

    for (rowMain, rowAction, i) in zip(board, actionBoard, range(len(actionBoard))):
        for (eachMain, eachAction, j) in zip(rowMain, rowAction, range(len(rowAction))):
            if eachMain == EMPTY:
                # print(actionBoard)
                # print(i)
                # print(j)
                # actionBoard[i][j]=player(board)
                setofactions.add((i, j))
    return (setofactions)

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard=copy.deepcopy(board)
    (row, column) = action
    newboard[row][column] = player(board)
    return newboard

    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # for loop for checking the vertical and horizontal wins
    for i in range(len(board)):
        # check if there is a win in vertical line
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
        # check if there is a win in horizontal line
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    # check if the main diagonal is a win
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    # check if the secondary diagonal is a win
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) == X or winner(board) == O:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                return False

    return True

    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    # raise NotImplementedError


def Max(param):
    pass


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """


    bestAction = None
    if board == terminal(board):
        return None
    # Maximizing Player
    elif player(board) == X:
        bestValueX = -math.inf
        for action in actions(board):
            valueX = minvalue(result(board, action))
            print("Value For Action:")
            print(action)
            print("Value")
            print(valueX)
            if valueX > bestValueX:
                bestValueX = valueX
                bestAction=action
        return bestAction
    elif player(board) == O:
        bestValueO = +math.inf
        for action in actions(board):
            valueO = maxvalue(result(board, action))
            print("Value For Action:")
            print(action)
            print("Value")
            print(valueO)
            if valueO < bestValueO:
                bestAction = action
                bestValueO=valueO
        return bestAction

    # raise NotImplementedError


def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    # print("bestmax value")
    # print(v)
    return v


# def Min(action):
#     pass


def minvalue(board):
    if terminal(board):
        return utility(board)
    v = +math.inf
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))

    # print("bestmin value")
    # print(v)
    return v


# def Max(action1)


def main():
    exm = [[X, O, EMPTY],
           [EMPTY, X, EMPTY],
           [EMPTY, EMPTY, EMPTY]]
    print(exm)
    print(winner(exm))
    # print(terminal(exm))
    # print(actions(exm))
    # print(result(exm,(2,1)))
    print(player(exm))
    print(minimax(exm))
    exm1 = [[X, O, EMPTY],
           [EMPTY, X, EMPTY],
           [EMPTY, EMPTY, O]]
    print(maxvalue(result(exm1,(2,2))))

if __name__ == '__main__':
    main()
