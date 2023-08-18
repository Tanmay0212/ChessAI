import numpy as np


BLACK , WHITE = 0 ,1
scoring= {'p': -1,
          'n': -3,
          'b': -3,
          'r': -5,
          'q': -9,
          'k': 0,
          'P': 1,
          'N': 3,
          'B': 3,
          'R': 5,
          'Q': 9,
          'K': 0,
          }

# def makeBoard():
#     board = np.zeros((2,8,8))

#     board[BLACK][0,0] = scoring.get('r')
#     board[BLACK][0,1] = scoring.get('n')
#     board[BLACK][0,2] = scoring.get('b')
#     board[BLACK][0,3] = scoring.get('q')
#     board[BLACK][0,4] = scoring.get('k')
#     board[BLACK][0,5] = scoring.get('b')
#     board[BLACK][0,6] = scoring.get('n')
#     board[BLACK][0,7] = scoring.get('r') 

#     board[WHITE][7,0] = scoring.get('R')
#     board[WHITE][7,1] = scoring.get('N')
#     board[WHITE][7,2] = scoring.get('B')
#     board[WHITE][7,3] = scoring.get('Q')
#     board[WHITE][7,4] = scoring.get('K')
#     board[WHITE][7,5] = scoring.get('B')
#     board[WHITE][7,6] = scoring.get('N')
#     board[WHITE][7,7] = scoring.get('R')

#     for i in range(8):
#         board[BLACK][1, i] = scoring.get('p')  # Black pawns
#         board[WHITE][6, i] = scoring.get('P')  # White pawns

    
#     return board

def validActions(state, row, col, turn):
    piece = state.board[turn][row, col]

    # Valid Moves for Black player
    #if turn == BLACK:
        
    # Black Pawn
    if piece == scoring.get('p'):
        moves = []
        if row < 7 and state.board[WHITE][row+1,col] == 0:
            moves.append((row+1, col))
            if row == 1 and state.board[WHITE][row+2,col] == 0:
                moves.append((row+2, col))
        if row < 7 and col > 0 and state.board[WHITE][row+1, col-1] != 0:
            moves.append((row+1,col-1))
        if row < 7 and col < 7 and state.board[WHITE][row+1, col+1] != 0:
            moves.append((row+1,col+1))
        return moves
    
    # Valid moves for white player
    #else:
        
    # White Pawn
    if piece == scoring.get('P'):
        moves = []
        if row > 0 and state.board[BLACK][row-1, col] == 0:
            moves.append((row-1, col))
            if row == 6 and state.board[BLACK][row-2, col] == 0 :
                moves.append(row-2, col)
        if row > 0 and col > 0 and state.board[BLACK][row - 1, col - 1] !=0 :
            moves.append((row-1, col-1))
        if row > 0 and col < 7 and state.board[BLACK][row - 1, col + 1] !=0 :
            moves.append(row-1, col+1)
        return moves

    
    # Black or white rook

    if piece == scoring.get('r') or piece == scoring.get('R'):
        moves = []

         # Check vertical moves upward
        for i in range(row - 1, -1, -1):
            if state.board[BLACK][i, col] == 0 and state.board[WHITE][i, col] == 0:
                moves.append((i, col))
            else:
                break

        # Check vertical moves downward
        for i in range(row + 1, 8):
            if state.board[BLACK][i, col] == 0 and state.board[WHITE][i, col] == 0:
                moves.append((i, col))
            else:
                break

        # Check horizontal moves to the left
        for j in range(col - 1, -1, -1):
            if state.board[BLACK][row, j] == 0 and state.board[WHITE][row, j] == 0:
                moves.append((row, j))
            else:
                break

        # Check horizontal moves to the right
        for j in range(col + 1, 8):
            if state.board[BLACK][row, j] == 0 and state.board[WHITE][row, j] == 0:
                moves.append((row, j))
            else:
                break
        
        return moves





