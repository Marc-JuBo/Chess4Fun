"""
Usuari fa les decisions
"""

import pygame as p
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #animació
IMAGES = {}

'''
inicialització del diccionari d'imatges
'''
def loadImages():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR","wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR","bp","wp"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/"+piece+".png"),(SQ_SIZE,SQ_SIZE))

'''
usuari inputa els gràfics
'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    playerClicks = [] #log dels clics que ha fet el jugador en tuples ex: ([(6,4),(5,4)])

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # ens dona un vector de coords (x,y)
                col = location[0]// SQ_SIZE
                row = location[1]// SQ_SIZE
                if gs.sqSelected == (row,col): #l'usuari clica el mateix quadre (esborrar selecció)
                    gs.sqSelected = ()
                    playerClicks = []
                else:
                    if(gs.board[row][col] != "--"): 
                        gs.sqSelected = (row,col)
                        playerClicks.append(gs.sqSelected) #append per clic dret i esquerre
                if len(playerClicks) == 2: # quan es clica la casella on es vol portar la peça
                    
                    pass



        drawGameState(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()


'''
responsable dels gràfics d'un gamestate
'''
def drawGameState(screen,gs):
    drawBoard(screen, gs)
    drawPieces(screen, gs)

def drawBoard(screen, gs):
    colors=[p.Color("white"),p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c)%2]
            p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))
            if gs.pieceSelected: 
                p.draw.rect(screen,"yellow",p.Rect(gs.sqSelected[1]*SQ_SIZE,gs.sqSelected[0]*SQ_SIZE,SQ_SIZE,SQ_SIZE))
                for r in range(DIMENSION):
                    for c in range(DIMENSION):
                        p.draw.circle(screen, "lightgray",((gs.possible[1]+0.51)*SQ_SIZE, (gs.sqSelected[0]+0.51)*SQ_SIZE), SQ_SIZE*0.3)


def drawPieces(screen,gs):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = gs.board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))


if __name__ == "__main__":
    main()