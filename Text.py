import pygame
from config import cell_size
pygame.font.init()
font = pygame.font.Font(None, int(cell_size*0.8))

def text_speech(sc, text, color, pos):
    rendered_text = font.render(text, True, color)
    sc.blit(rendered_text, rendered_text.get_rect(center=pos))