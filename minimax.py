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
blackPieces = ['p','n','b','r','q','k']
whitePieces = ['P','N','B','R','Q','K']



def getBlackPawnPos(board):
    pos = np.where(board == 'p')
    return list(zip(pos[0], pos[1]))
    

def getBlackRookPos(board):
    pos = np.where(board == 'r')
    return list(zip(pos[0], pos[1]))

def getBlackBishopPos(board):
    pos = np.where(board == 'b')
    return list(zip(pos[0], pos[1]))

def getBlackKnightPos(board):
    pos = np.where(board == 'n')
    return list(zip(pos[0], pos[1]))

def getBlackQueenPos(board):
    pos = np.where(board == 'q')
    return list(zip(pos[0], pos[1]))

def getBlackKingPos(board):
    pos = np.where(board == 'k')
    return list(zip(pos[0], pos[1]))

def blackPawnValidMov(board, pos):
    valid_states = []
    for row,col in pos :
        current_board = board.copy()
        if row < 7 and board[row+1,col] == 'E':
            current_board[row+1,col] == 'p'
            current_board[row,col] == 'E'
            valid_states.append(current_board)
            current_board = board.copy()
            if row == 1 and board[row+2,col] == 'E':
                current_board[row+2,col] == 'p'
                current_board[row,col] == 'E'
                valid_states.append(current_board)
                current_board = board.copy()
        if row < 7 and col > 0 and board[row+1, col-1] in whitePieces:
            current_board[row+1, col-1] = 'p'
            current_board[row,col] = 'E'
            valid_states.append(current_board)
            current_board = board.copy()
        if row < 7 and col < 7 and board[row+1, col+1] in whitePieces:
            current_board[row+1,col+1] = 'p'
            current_board[row,col] = 'E'
            valid_states.append(current_board)
            current_board = board.copy()
    return valid_states   


def blackRookValidMov(board, pos):
    valid_states = []
    for row, col in pos:
        current_board = board.copy()
         # Check vertical moves upward
        for i in range(row - 1, -1, -1):
            if board[i, col] == 'E' or board[i, col] not in blackPieces:
                current_board[i,col] = 'r'
                current_board[row,col] = 'E'
                valid_states.append(current_board)
            else:
                break

        # Check vertical moves downward
        for i in range(row + 1, 8):
            current_board = board.copy()
            if board[i, col] == 'E' or board[i, col] not in blackPieces:
                current_board[i,col] = 'r'
                current_board[row,col] = 'E'
                valid_states.append(current_board)
            else:
                break

        # Check horizontal moves to the left
        for j in range(col - 1, -1, -1):
            current_board = board.copy()
            if board[row, j] == 'E' or board[row, j] not in blackPieces:
                current_board[row,j] = 'r'
                current_board[row,col] = 'E'
                valid_states.append(current_board)
            else:
                break

        # Check horizontal moves to the right
        for j in range(col + 1, 8):
            current_board = board.copy()
            if board[row, j] == 'E' or board[row, j] not in blackPieces:
                current_board[row,j] = 'r'
                current_board[row,col] = 'E'
                valid_states.append(current_board)
            else:
                break
    return valid_states




def validActions1(state):
    state.whiteToMove = False

    if state.whiteToMove == False:

        #Black Pawn
        pos = getBlackPawnPos(state.board)
        print("Pawn Positions: ")
        print(pos)
        valid_states = []
        valid_states.append(blackPawnValidMov(state.board, pos))
        

        #Black rook
        pos = getBlackRookPos(state.board)
        print("Rook Positions :")
        print(pos)
        valid_states.append(blackRookValidMov(state.board,pos))

        return valid_states

            
            
        



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

    #Black or WHite knight

    if piece == scoring['n'] or piece == scoring['N']:  # Knight (both white and black)
            valid_moves = []

            # Knight moves (L-shaped)
            knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

            for dr, dc in knight_moves:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    dest_piece = state.board[self.current_player, new_row, new_col]
                    if dest_piece == 0 or self.is_opponent_piece(new_row, new_col):
                        valid_moves.append((new_row, new_col))

            return valid_moves






def minimax(state):
    currentState = state.copy()
    all_valid_actions = valid_actions(state)
    best_action = get_best_move(all_valid_actions)
    currentState = best_action
    return best_action
    state.whiteToMove = not state.whiteToMove
    minimax(state)




