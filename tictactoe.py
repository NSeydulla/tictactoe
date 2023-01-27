import pygame
import time
from Game import Game
from settings import cell_size, sc_h, sc_w

def main():
    while 1:
        MOUSEMOTION = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if Game.winned: Game.initGame(screen)
                else: Game.onClick(screen, event.pos)

            MOUSEMOTION = event.type == pygame.MOUSEMOTION or MOUSEMOTION

        if MOUSEMOTION and not Game.winned:
            mousePos = pygame.mouse.get_pos()
            for column in Game.cells:
                for cell in column:
                    cell.checkHover(screen, cell.collidepoint(mousePos))

        pygame.display.update()
        clock.tick(20)


pygame.init()
screen = pygame.display.set_mode((sc_w, sc_h))
pygame.display.set_caption("tic tac toe")
clock = pygame.time.Clock()

Game = Game(screen)
main()

pygame.quit()
quit()