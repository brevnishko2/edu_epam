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
        # find winner and check is finished
        for line in some_board:
            if ("x" not in line or "o" not in line) and "-" not in line:
                win = line[0]
            elif "-" in line:
                unfinished = True

    diagonal: List[list] = [[], []]
    for i in range(len(board)):
        j = len(board) - i - 1
        diagonal[0].append(board[i][i])
        diagonal[1].append(board[j][i])

    find_win(board)
    find_win(reverse_board(board))
    find_win(diagonal)

    if win:
        return str(win) + " wins!"
    elif unfinished:
        return "unfinished"
    else:
        return "draw!"
