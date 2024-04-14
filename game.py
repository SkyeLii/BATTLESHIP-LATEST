import pygame
import sys
import os
import Button
import math
import random


pygame.init()

def get_file(name):
	return os.path.join(os.path.dirname(__file__), name)

player_board = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
				['A', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['B', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['C','W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['D','W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['E', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['F', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['G', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['H', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['I', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['J', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]
computer_board = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
				['A', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['B', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['C','W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['D','W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['E', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['F', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['G', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['H', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['I', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
				['J', 'W','W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']]
player_visuals = []
computer_visuals = []
player_ships = list()
computer_ships = list()


clock = pygame.time.Clock()
w = pygame.display.Info().current_w
h = pygame.display.Info().current_h
bg = pygame.transform.scale(pygame.image.load(get_file('bg.jpg')), (w, h))
logo = pygame.transform.scale(pygame.image.load(get_file('logo.png')), (w * 0.15, h * 0.07))
logo_w = logo.get_width()
logo_h = logo.get_height()
logo_point = (w / 2 - logo_w/2, h * 0.03)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Battleship")

loading = pygame.image.load(get_file('loading.png'))
loading_w = loading.get_width()
loading_point = (w / 2 - loading_w/2, h * 0.07)

s = w * 0.033
tile_size = (s, s)
def init_boards():
	
	letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


	print(player_board)

	index = "W"
	for i in range(11):
		player_row = []
		computer_row = []
		for j in range(11):
			if i == 0:
				index = j
			elif j == 0:
				index = letters[i-1]
			else:
				index = "W"

			p_image = pygame.image.load(get_file(f"P_{index}.png")).convert_alpha()
			c_image = pygame.image.load(get_file(f"C_{index}.png")).convert_alpha()

			img_w = p_image.get_width() * 0.073 + 1
			p_img_x = j * img_w + w * 0.04
			p_img_y = i * img_w + h * 0.15 
			c_img_x = j * img_w + w * 0.57 
			c_img_y = i * img_w + h * 0.15
			
			player_row.append(Button.Button(p_img_x, p_img_y, p_image, p_image, 0.073))
			computer_row.append(Button.Button(c_img_x, c_img_y, c_image, c_image, 0.073))


		player_visuals.append(player_row)
		computer_visuals.append(computer_row)



ships = ["Aircraft_Carrier", "Battleship", "Destroyer", "Submarine", "Cruiser"]
sizes = {"Aircraft_Carrier":5,  "Battleship":4, "Destroyer":3, "Submarine":3,"Cruiser":2  }
ships_img = []
ships_rect = []
for s in ships:
	img = pygame.transform.scale(pygame.image.load(get_file(f'{s}.png')), (w * 0.2, h * 0.1))
	ships_img.append(img)
	ships_rect.append(img.get_rect())

start_image = pygame.image.load(get_file(f"button_start.png")).convert_alpha()
start_hover_img = pygame.image.load(get_file(f"button_start_hover.png")).convert_alpha()
start_img_w = start_image.get_width()
start_img_x = w / 2 - start_img_w / 2
start_img_y = h * 0.9
start_btn = Button.Button(start_img_x, start_img_y, start_image, start_hover_img, 1)

quit_image = pygame.image.load(get_file(f"button_quit.png")).convert_alpha()
quit_hover_img = pygame.image.load(get_file(f"button_quit_hover.png")).convert_alpha()
quit_img_w = quit_image.get_width()
quit_img_x = w / 2 - quit_img_w / 2
quit_img_y = h * 0.9
quit_btn = Button.Button(quit_img_x, quit_img_y, quit_image, quit_hover_img, 1)

flip_image = pygame.image.load(get_file(f"button_flip.png")).convert_alpha()
flip_hover_img = pygame.image.load(get_file(f"button_flip_hover.png")).convert_alpha()
flip_img_w = flip_image.get_width()
flip_img_x = w / 1.1 - flip_img_w / 2
flip_img_y = h * 0.8
flip_btn = Button.Button(flip_img_x, flip_img_y, flip_image, flip_hover_img, 0.8)

def init(screen):
	run = True
	while run:
		screen.blit(bg, (0, 0))
		screen.blit(logo, logo_point)
		screen.blit(loading, loading_point)
		
		if start_btn.draw(screen):
			run = False
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
			init_boards()
			place_ships(screen)

		if (start_btn.hover(screen)):
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
		else:
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
			
		clock.tick(100)
		for event in pygame.event.get():		
		
			if event.type == pygame.QUIT:
				run = False
			
				

	
		pygame.display.flip()
		pygame.display.update()
	
def init_computer():
	random.seed()
	ind = 0
	while ind < len(ships):
		ship = ships[ind]
		horizontal = random.randint(0,1)
		i = random.randint(1, 10)
		j = random.randint(1, 10)
	
		no_crossing = True
		l = sizes.get(ship)
		if horizontal:
			if (j + l) > 11:
				no_crossing = False
				continue
			for k in range(l):
				if computer_board[i][j+k] != "W":
					no_crossing = False
					continue 
		else:
			if (i + l) > 11:
				no_crossing = False
				continue
			for k in range(l):
				if computer_board[i+k][j] != "W":
					no_crossing = False
					continue 

		if no_crossing:
			ii, jj = i, j
						
			for k in range(l):
				if horizontal:
					jj = j + k
				else:
					ii = i + k		
								
				computer_board[ii][jj] = f"{ship}_{k}"
				computer_ships.append((ii,jj))
			ind += 1
				

def place_ships(screen):
	init_computer()
	
	run = True
	ind = 0
	horizontal = True
	while run and ind < len(ships):
		if horizontal:
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
		else:
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
		screen.blit(bg, (0, 0))
		screen.blit(logo, logo_point)
		clock.tick(100)
		ship = ships[ind]
		ship_panel = pygame.transform.scale(pygame.image.load(get_file(f'{ship}_panel.png')), (w * 0.45, h* 0.55))
		screen.blit(ship_panel, (w * 0.5, h * 0.2))

		if flip_btn.draw(screen):
			if horizontal:
				horizontal = False
				pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
			else:
				horizontal = True
				pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)

	
		for event in pygame.event.get():		
		
			if event.type == pygame.QUIT:
				run = False
					

		
		for i in range(11):
			for j in range(11):
				
								
				if player_visuals[i][j].draw(screen):
					no_crossing = True
					l = sizes.get(ship)
					if horizontal:
						if (j + l) > 11:
							no_crossing = False
							break
						for k in range(l):
							if player_board[i][j+k] != "W":
								no_crossing = False
								break 
					else:
						if (i + l) > 11:
							no_crossing = False
							break
						for k in range(l):
							if player_board[i+k][j] != "W":
								no_crossing = False
								break 
					if no_crossing:
						ii, jj = i, j
						
						for k in range(l):
							name = f"P_W_{ship}_{k}.png"
							new_img = pygame.image.load(get_file(name)).convert_alpha()
							if horizontal:
								jj = j + k
							else:
								ii = i + k		
								new_img = pygame.transform.rotate(pygame.image.load(get_file(name)).convert_alpha(), -90)			
							player_board[ii][jj] = f"{ship}_{k}"
							player_visuals[ii][jj].update(new_img)
							player_visuals[ii][jj].draw(screen)
							player_ships.append((ii, jj))
						ind += 1
					

		if quit_btn.draw(screen):
			run = False
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
			

		if (quit_btn.hover(screen)):
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
		
		
			

		
		pygame.display.flip()
		pygame.display.update()
	print(player_board)
	if run:
		play(screen)

def play(screen):
	run = True
	
	player_turn = True

	while run:

		screen.blit(bg, (0, 0))
		screen.blit(logo, logo_point)
	
		
		clock.tick(100)
		

		for i in range(11):
			for j in range(11):
				player_visuals[i][j].draw(screen)
				computer_visuals[i][j].draw(screen)

		for event in pygame.event.get():		
		
			if event.type == pygame.QUIT:
				run = False

			if len(computer_ships) == 0:
				run = False
				endgame("player")
				
			if len(player_ships) == 0:
				run == False
				endgame("computer")
			
			if player_turn:

				
				for i in range(11):
					for j in range(11):				
								
						if computer_visuals[i][j].draw(screen):
							name = f"missed_W.png"
							if computer_board[i][j] != "W":
								name = f"C_W_hit.png"
								if (i,j) in computer_ships:
									computer_ships.remove((i,j))

							new_img = pygame.image.load(get_file(name)).convert_alpha()
					
							computer_visuals[i][j].update(new_img)
							computer_visuals[i][j].draw(screen)
							
							player_turn = False
			else:
				
				random.seed()
				i = random.randint(1, 10)
				j = random.randint(1, 10)
				name = f"missed_W.png"
				print(i,j)
				if player_board[i][j] != "W":
					name = f"C_W_hit.png"
					if (i,j) in player_ships:
						player_ships.remove((i,j))

				new_img = pygame.image.load(get_file(name)).convert_alpha()
					
				player_visuals[i][j].update(new_img)
				player_visuals[i][j].draw(screen)
				
				player_turn = True
	



		if quit_btn.draw(screen):
			run = False
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
			

		if (quit_btn.hover(screen)):
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
		else:
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
	
		pygame.display.flip()
		pygame.display.update()
	pygame.quit()

def endgame(winner):
	run = True
	while run:
		victory = pygame.image.load(get_file(f'{winner}_wins.png'))
		screen.blit(bg, (0, 0))
		screen.blit(logo, logo_point)
		screen.blit(victory, loading_point)
		
		if quit_btn.draw(screen):
			run = False
			pygame.quit()

		if (quit_btn.hover(screen)):
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
		else:
			pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
			
		clock.tick(100)
		for event in pygame.event.get():		
		
			if event.type == pygame.QUIT:
				run = False
			
				

	
		pygame.display.flip()
		pygame.display.update()
