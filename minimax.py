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
            current_board[row+1,col] = 'p'
            current_board[row,col] = 'E'
            valid_states.append(current_board)
            current_board = board.copy()
            if row == 1 and board[row+2,col] == 'E':
                current_board[row+2,col] = 'p'
                current_board[row,col] = 'E'
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
        print(row,col)
        current_board = board.copy()
         # Check vertical moves upward
        for i in range(row - 1, -1, -1):
            if board[i, col] == 'E' or board[i, col] not in blackPieces:
                if board[i+1,col] not in whitePieces: # To make sure rook does not jump over a white piece
                    current_board[i,col] = 'r'
                    current_board[row,col] = 'E'
                    valid_states.append(current_board)
            else:
                break

        # Check vertical moves downward
        for i in range(row + 1, 8):
            current_board = board.copy()
            if board[i, col] == 'E' or board[i, col] not in blackPieces:
                if board[i-1,col] not in whitePieces:  # To make sure rook does not jump over a white piece
                    current_board[i,col] = 'r'
                    current_board[row,col] = 'E'
                    valid_states.append(current_board)
            else:
                break

        # Check horizontal moves to the left
        for j in range(col - 1, -1, -1):
            current_board = board.copy()
            if board[row, j] == 'E' or board[row, j] not in blackPieces:
                if board[row,j+1] not in whitePieces:
                    current_board[row,j] = 'r'  
                    current_board[row,col] = 'E'
                    valid_states.append(current_board)
            else:
                break

        # Check horizontal moves to the right
        for j in range(col + 1, 8):
            current_board = board.copy()
            if board[row, j] == 'E' or board[row, j] not in blackPieces:
                if board[row,j-1] not in whitePieces:
                    current_board[row,j] = 'r'
                    current_board[row,col] = 'E'
                    valid_states.append(current_board)
            else:
                break
    return valid_states



def blacknightValidMov(board,pos):
    # Define the valid moves for a black knight
    knight_moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]
    valid_states = []
    for knight_position in pos:
        row, col = knight_position
        for move in knight_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8 and board[new_row, new_col] not in blackPieces:
                current_board = board.copy()
                current_board[new_row, new_col] = 'n'  # Move to the new position
                current_board[row, col] = 'E'  # Clear the knight's previous position
                valid_states.append(current_board)
    
    return valid_states

def blackBishopValidMov(board,pos):
    # Define the valid moves for a bishop (diagonal moves)
    bishop_moves = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    valid_states = []
    for bishop_position in pos:
        row, col = bishop_position
        for dr, dc in bishop_moves:
            new_row, new_col = row + dr, col + dc
            while 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row, new_col] in blackPieces:
                    break
                current_board = board.copy()
                current_board[new_row, new_col] = 'b'  # Move to the new position
                current_board[row, col] = 'E'  # Clear the bishop's previous position
                valid_states.append(current_board)

                #if board[new_row, new_col] in whitePieces:
                #    break  # Cannot move past your own pieces
                new_row += dr
                new_col += dc

    return valid_states









def validActions(state):
    state.whiteToMove = False

    if state.whiteToMove == False:
        valid_states = []

        #Black Pawn
        #pos = getBlackPawnPos(state.board)
        #valid_states.append(blackPawnValidMov(state.board, pos))
        

        #Black rook
        #pos = getBlackRookPos(state.board)
        #print("Rook Positions :")
        #print(pos)
        #valid_states.append(blackRookValidMov(state.board,pos))


        #Black Knight
        #pos = getBlackKnightPos(state.board)
        #valid_states.append(blacknightValidMov(state.board,pos))

        #Black Bishop
        pos = getBlackBishopPos(state.board)
        valid_states.append(blackBishopValidMov(state.board,pos))

        return valid_states

            
            
        

def minimax(state):
    currentState = state.copy()
    all_valid_actions = valid_actions(state)
    best_action = get_best_move(all_valid_actions)
    currentState = best_action
    return best_action
    state.whiteToMove = not state.whiteToMove
    minimax(state)




