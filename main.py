import pygame
import time
from config import *

def text_speech(font, text, color, xy, bold=0):
	font.set_bold(bold)
	rendered_text = font.render(text, True, color)
	text_rect = rendered_text.get_rect(center=xy)
	sc.blit(rendered_text, text_rect)

def Winned():
	for i in range(3):
		if ((cells_name[i][0] == cells_name[i][1] == cells_name[i][2] != '') or
			(cells_name[0][i] == cells_name[1][i] == cells_name[2][i] != '')):
			return True
	if ((cells_name[0][0] == cells_name[1][1] == cells_name[2][2] != '') or
		(cells_name[0][2] == cells_name[1][1] == cells_name[2][0] != '')):
		return True

def game_loop():
	global cur, cells_name, winned
	while 1:
		# Обработка ивентов(клик, вводить мышкой, нажатие клавиши и т.д)
		for event in pygame.event.get():
			# Выход
			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_F4 and event.mod == 256):
				pygame.quit(); quit()

			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not winned:
				for i, arr in enumerate(cells):
					for j, cell in enumerate(arr):
						if cell.collidepoint(event.pos):
							if cells_name[i][j] == '':
								cells_name[i][j] = cur
								cur = oth[cur]

								if Winned():
									winned = True
									cur = oth[cur]

		# Рисовальня

		sc.fill(WHITE)
		for i in range(3):
			for j in range(3):
				text_speech(font, cells_name[i][j], BLACK, (j*cell_size+cell_size//2, i*cell_size+cell_size//2))
			pygame.draw.line(sc, BLACK, [cell_size*i, 0], [cell_size*i, sc_w])
			pygame.draw.line(sc, BLACK, [0, cell_size*i], [sc_w, cell_size*i])

		if winned: text_speech(font, f'{cur} выйграл!', RED, (sc_w//2,sc_h//2))

		pygame.display.update()

pygame.init()
pygame.font.init()
sc = pygame.display.set_mode((sc_w, sc_h))
pygame.display.set_caption("tic tac toe")
font = pygame.font.Font(None, 45)

game_loop()
pygame.quit()
quit()