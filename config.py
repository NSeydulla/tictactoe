import pygame

cell_size = 60
cells = [[pygame.Rect(cell_size*j, cell_size*i, cell_size, cell_size) for j in range(3)] for i in range(3)]
cells_name = [['' for j in range(3)] for i in range(3)]

sc_w = cell_size*3
sc_h = cell_size*3

cur = 'x'
oth = {'x': 'o', 'o': 'x'}
winned = False

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)