"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List
from copy import deepcopy


def reverse_board(some_board: List[list]) -> List[list]:
    """Reverse square matrix from 1,2  to  1,3
                                  3,4      2,4
    Args:
        some_board: len(List) should be eq to len(List[list])

    Returns:
        reversed matrix

    """
    reversed_board: List[list] = [[] for _ in some_board]
    for i in range(len(some_board)):
        for j in range(len(some_board)):
            reversed_board[i].append(some_board[j][i])
    return reversed_board


def tic_tac_toe_checker(board: List[List]) -> str:
    """Find winner if it is or check for draw-unfinished game

    Args:
        board: len(List) should be eq to len(List[list])

    Returns:
        str: 'x wins!' if x win this game
            'draw' if there is no winner and game cant be continued
            'unfinished' if game is not finished

    """
    unfinished = False
    win = False

    def find_win(some_board):
        nonlocal win
        nonlocal unfinished
        diagonal1, diagonal2 = [], []
        board_with_diag = deepcopy(some_board)

        # append diagonals to the board
        for i in range(len(some_board)):
            j = len(some_board) - i - 1
            diagonal1.append(some_board[i][i])
            diagonal2.append(some_board[j][i])
        board_with_diag.append(diagonal1)
        board_with_diag.append(diagonal2)

        # find winner and check is finished
        for line in board_with_diag:
            if ("x" not in line or "o" not in line) and "-" not in line:
                win = line[0]
            elif "-" in line:
                unfinished = True

    find_win(board)
    find_win(reverse_board(board))

    if win:
        return str(win) + " wins!"
    elif unfinished:
        return "unfinished"
    else:
        return "draw!"
