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

class GameState:
    def __init__(self):
        self.board = np.zeros((2,8,8))
        self.board[BLACK][0,0] = scoring.get('r')
        self.board[BLACK][0,1] = scoring.get('n')
        self.board[BLACK][0,2] = scoring.get('b')
        self.board[BLACK][0,3] = scoring.get('q')
        self.board[BLACK][0,4] = scoring.get('k')
        self.board[BLACK][0,5] = scoring.get('b')
        self.board[BLACK][0,6] = scoring.get('n')
        self.board[BLACK][0,7] = scoring.get('r') 

        self.board[WHITE][7,0] = scoring.get('R')
        self.board[WHITE][7,1] = scoring.get('N')
        self.board[WHITE][7,2] = scoring.get('B')
        self.board[WHITE][7,3] = scoring.get('Q')
        self.board[WHITE][7,4] = scoring.get('K')
        self.board[WHITE][7,5] = scoring.get('B')
        self.board[WHITE][7,6] = scoring.get('N')
        self.board[WHITE][7,7] = scoring.get('R')

        for i in range(8):
            self.board[BLACK][1, i] = scoring.get('p')  # Black pawns
            self.board[WHITE][6, i] = scoring.get('P')  # White pawns

        self.whiteToMove = True
        self.moveLog = []

        