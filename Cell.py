import pygame
from Text import text_speech

class Cell():
    def __init__(self, rect, color=(120, 190, 197)):
        self.rect = rect
        self.color = color
        self.collidepoint = self.rect.collidepoint
        self.text=''

    def render(self, sc):
        pygame.draw.rect(sc, self.color, self.rect, 0, 13)
        text_speech(sc, self.text, (255,255,255), self.rect.center)

    def setText(self, text):
        self.text=text
        self.color=(120,190,197)

    def checkHover(self, sc, isHovered):
        lastColor = self.color
        self.color = (61,66,80) if isHovered and self.text=='' else (120,190,197)
        if lastColor != self.color: self.render(sc)