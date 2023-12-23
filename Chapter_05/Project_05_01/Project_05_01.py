"""
Chess Dictionary Validator
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen',
'2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board.
Write a function named isValidChessBoard() that takes a dictionary argument
and returns True or False depending on if the board is valid.
A valid board will have exactly one black king and exactly one white
king. Each player can only have at most 16 pieces, at most 8 pawns, and
all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t
be on space '9z'. The piece names begin with either a 'w' or 'b' to represent
 white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or
'king'. This function should detect when a bug has resulted in an improper
chess board.

@author Sharaf Qeshta
"""


def isValidChessBoard(board):
    """Validate counts and location of pieces on board"""

    # Define pieces and colors
    pieces = ['king', 'queen', 'rook', 'knight', 'bishop', 'pawn']
    colors = ['b', 'w']
    # Set of all chess pieces
    all_pieces = set(color + piece for piece in pieces for color in colors)

    # Define valid range for count of chess pieces by type (low, high) tuples
    valid_counts = {'king': (1, 1),
                    'queen': (0, 1),
                    'rook': (0, 2),
                    'bishop': (0, 2),
                    'knight': (0, 2),
                    'pawn': (0, 8)}

    # Get count of pieces on the board
    piece_cnt = {}
    for v in board.values():
        if v in all_pieces:
            piece_cnt.setdefault(v, 0)
            piece_cnt[v] += 1

    # Check if there are a valid number of pieces
    for piece in all_pieces:
        cnt = piece_cnt.get(piece, 0)
        lo, hi = valid_counts[piece[1:]]
        if not lo <= cnt <= hi:  # Count needs to be between lo and hi
            if lo != hi:
                print(f"There should between {lo} and {hi} {piece} but there are {cnt}")
            else:
                print(f"There should be {lo} {piece} but there are {cnt})")
            return False

    # Check if locations are valid
    for location in board.keys():
        row = int(location[:1])
        column = location[1:]
        if not ((1 <= row <= 8) and ('a' <= column <= "h")):
            print(f"Invaid to have {board[location]} at postion {location}")
            return False

    # Check if all pieces have valid names
    for loc, piece in board.items():
        if piece:
            if not piece in all_pieces:
                print(f"{piece} is not a valid chess piece at postion {loc}")
                return False

    return True
