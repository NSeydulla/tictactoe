import pygame
from Cell import Cell
from config import cell_size, indent, sc_h, sc_w
from Text import text_speech

class Game():
    def __init__(self, sc):
        self.cells = [[Cell(pygame.Rect(cell_size*j+indent*j, cell_size*i+indent*i, cell_size, cell_size)) for j in range(3)] for i in range(3)]
        self.initGame(sc)
    
    def initGame(self, sc):
        sc.fill((255,255,255))
        for col in self.cells:
            for cell in col:
                cell.setText('')
                cell.render(sc)
        self.activePlayer = 'x'
        self.winned = False
        self.counter = 0

    def onClick(self, sc, pos):
        self.counter += 1
        for column in self.cells:
            for cell in column:
                if cell.collidepoint(pos):
                    if cell.text == '':
                        cell.setText(self.activePlayer)
                        cell.render(sc)
                        self.activePlayer = 'o' if self.activePlayer == 'x' else 'x'
                        self.checkWin(sc, cell.text)
                    return

    def checkWin(self, sc, winner):
        self.winned = ((self.cells[0][0].text == self.cells[1][1].text == self.cells[2][2].text != '') or
                (self.cells[0][2].text == self.cells[1][1].text == self.cells[2][0].text != ''))
        for i in range(3):
            if ((self.cells[i][0].text == self.cells[i][1].text == self.cells[i][2].text != '') or
                (self.cells[0][i].text == self.cells[1][i].text == self.cells[2][i].text != '')):
                self.winned = True
        if self.winned: text_speech(sc, f'{winner} выйграл!', (240,30,30), (sc_w//2,sc_h//2))
        elif self.counter == 9:
            self.winned = True
            text_speech(sc, f'Ничья!', (240,30,30), (sc_w//2,sc_h//2))