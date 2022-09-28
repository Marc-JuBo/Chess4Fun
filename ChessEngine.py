<<<<<<< Updated upstream
"""
- té tota la informació de l'estat de joc
- responsable de determinar els moviments vàlids
- tindrà un log dels moviments
"""

from http.client import SWITCHING_PROTOCOLS


class GameState():
    def __init__(self):
        # Tauler actual
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]

        # Peça seleccionada, i tauler (binari) de possibles moviments d'aquesta peça
        self.pieceSelected = False 
        self.sqSelected = () #és un log de la última (row,col) que ha premut el jugador
        self.possible = [[0 for col in range(8)] for row in range(8)]


        self.whiteToMove = True
        self.moveLog = []

class Move():
    def __init__(self,startSq,endSq,board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow,self.startRow]
        self.pieceCaptured = board[self.endRow,self.endCol]


def tryPossible(gs):
    pass
=======
"""
- té tota la informació de l'estat de joc
- responsable de determinar els moviments vàlids
- tindrà un log dels moviments
"""

from Parameters import *

from http.client import SWITCHING_PROTOCOLS


class GameState():
    def __init__(self):
        # Tauler actual
        self.whiteDown = True
        if(self.whiteDown):
            self.board = [
                ["bR", "bp", "--", "--", "--", "--", "wp", "wR"],
                ["bN", "bp", "--", "--", "--", "--", "wp", "wN"],
                ["bB", "bp", "--", "--", "--", "--", "wp", "wB"],
                ["bQ", "bp", "--", "--", "--", "--", "wp", "wQ"],
                ["bK", "bp", "--", "--", "--", "--", "wp", "wK"],
                ["bB", "bp", "--", "--", "--", "--", "wp", "wB"],
                ["bN", "bp", "--", "--", "--", "--", "wp", "wN"],
                ["bR", "bp", "--", "--", "--", "--", "wp", "wR"],
            ]

        else:
            self.board = [
                ["wR", "wp", "--", "--", "--", "--", "bp", "bR"],
                ["wN", "wp", "--", "--", "--", "--", "bp", "bN"],
                ["wB", "wp", "--", "--", "--", "--", "bp", "bB"],
                ["wQ", "wp", "--", "--", "--", "--", "bp", "bQ"],
                ["wK", "wp", "--", "--", "--", "--", "bp", "bK"],
                ["wB", "wp", "--", "--", "--", "--", "bp", "bB"],
                ["wN", "wp", "--", "--", "--", "--", "bp", "bN"],
                ["wR", "wp", "--", "--", "--", "--", "bp", "bR"],
            ]

        # Peça seleccionada, i tauler (binari) de possibles moviments d'aquesta peça
        self.kingHasMoved = False
        self.pieceSelected = False 
        self.sqSelected = () #és un log de la última (row,col) que ha premut el jugador
        self.posible = [[0 for col in range(8)] for row in range(8)]
         # Mostra les possibles opcions de moviment:
            # 0 no té opció d'arribar-hi
            # 1 té opció d'arribar-hi
            # 2 té opció de capturar peça

        self.whiteToMove = True
        self.moveLog = []

        
def tryPosible(gs):
    gs.posible = [[0 for col in range(8)] for row in range(8)]
    sqc = gs.sqSelected[0]
    sqr = gs.sqSelected[1]
    piece =  gs.board[gs.sqSelected[0]][gs.sqSelected[1]]
    # Ara mirarem peça per peça, tots els casos. 
    pieceColor = piece[0]
    if pieceColor == 'w': 
        enemyColor = 'b' 
    else: 
        enemyColor = 'w'          
    if piece[1] == 'p': # Comencem mirant els peons.
        if (gs.whiteDown and pieceColor == 'w') or (not gs.whiteDown and pieceColor == 'b'): 
            # Mirem primer els peons de sota.
            if(gs.board[sqc][sqr-1] == "--"):
                gs.posible[sqc][sqr-1] = 1
                if(sqr == 6 and gs.board[sqc][sqr-2] == "--"): 
                    gs.posible[sqc][sqr-2] = 1
            if(gs.board[sqc+1][sqr-1][0] == enemyColor and sqr != 7):
                gs.posible[sqc+1][sqr-1] = 2
            if(gs.board[sqc-1][sqr-1][0] == enemyColor and sqr != 0):
                gs.posible[sqc-1][sqr-1] = 2  
        else:
        # Mirem ara els peons de sobre.
            if(gs.board[sqc][sqr+1] == "--"):
                gs.posible[sqc][sqr+1] = 1
                if(sqr == 1 and gs.board[sqc][sqr+2] == "--"): 
                    gs.posible[sqc][sqr+2] = 1
            if(gs.board[sqc+1][sqr+1][0] == enemyColor and sqr != 7):
                gs.posible[sqc+1][sqr+1] = 2
            if(gs.board[sqc-1][sqr+1][0] == enemyColor and sqr != 0):
                gs.posible[sqc-1][sqr+1] = 2  
            

        

    

class Move():
    def __init__(self,startSq,endSq,board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow,self.startRow]
        self.pieceCaptured = board[self.endRow,self.endCol]


>>>>>>> Stashed changes
