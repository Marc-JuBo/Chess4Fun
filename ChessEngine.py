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