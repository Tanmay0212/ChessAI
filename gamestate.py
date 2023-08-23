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

        self.board = np.zeros((8,8), dtype=object)
        self.board[0,0] = 'r'
        self.board[0,1] = 'n'
        self.board[0,2] = 'b'
        self.board[0,3] = 'q'
        self.board[0,4] = 'k'
        self.board[0,5] = 'b'
        self.board[0,6] = 'n'
        self.board[0,7] = 'r' 

        self.board[7,0] = 'R'
        self.board[7,1] = 'N'
        self.board[7,2] = 'B'
        self.board[7,3] = 'Q'
        self.board[7,4] = 'K'
        self.board[7,5] = 'B'
        self.board[7,6] = 'N'
        self.board[7,7] = 'R'

        for i in range(8):
            self.board[1, i] = 'p'  # Black pawns
            self.board[6, i] = 'P'  # White pawns
        
        #self.board[1,0] = 'E'
        #self.board[1,6] = 'E'

        # Replace 0 with None using NumPy masking
        self.board[self.board == 0] = 'E'

        # self.board = np.zeros((8,8))
        # self.board[0,0] = scoring.get('r')
        # self.board[0,1] = scoring.get('n')
        # self.board[0,2] = scoring.get('b')
        # self.board[0,3] = scoring.get('q')
        # self.board[0,4] = scoring.get('k')
        # self.board[0,5] = scoring.get('b')
        # self.board[0,6] = scoring.get('n')
        # self.board[0,7] = scoring.get('r') 

        # self.board[7,0] = scoring.get('R')
        # self.board[7,1] = scoring.get('N')
        # self.board[7,2] = scoring.get('B')
        # self.board[7,3] = scoring.get('Q')
        # self.board[7,4] = scoring.get('K')
        # self.board[7,5] = scoring.get('B')
        # self.board[7,6] = scoring.get('N')
        # self.board[7,7] = scoring.get('R')

        # for i in range(8):
        #     self.board[1, i] = scoring.get('p')  # Black pawns
        #     self.board[6, i] = scoring.get('P')  # White pawns

        self.whiteToMove = True
        self.blackPieces = 16
        self.whitePieces = 16
        self.moveLog = []

        